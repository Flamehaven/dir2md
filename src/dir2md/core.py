from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
import json

from .gitignore import build_gitignore_matcher
from .markdown import to_markdown
from .simhash import simhash64, hamming
from .summary import summarize
from .manifest import sha256_bytes, write_manifest
from .token import estimate_tokens
from .masking import apply_masking

@dataclass
class Stats:
    total_dirs: int = 0
    total_files_in_tree: int = 0
    total_omitted: int = 0
    total_with_contents: int = 0
    est_tokens_prompt: int = 0

@dataclass
class Config:
    root: Path
    output: Path
    include_globs: List[str]
    exclude_globs: List[str]
    omit_globs: List[str]
    respect_gitignore: bool
    follow_symlinks: bool
    max_bytes: Optional[int]
    max_lines: Optional[int]
    include_contents: bool
    only_ext: Optional[set[str]] = None
    add_stats: bool = True
    add_toc: bool = False
    # Preset/token related
    llm_mode: str = "ref"   # off|ref|summary|inline
    budget_tokens: int = 6000
    max_file_tokens: int = 1200
    dedup_bits: int = 16
    sample_head: int = 120
    sample_tail: int = 40
    strip_comments: bool = False
    emit_manifest: bool = True
    preset: str = "iceberg"
    explain_capsule: bool = False
    no_timestamp: bool = False
    masking_mode: str = "basic"

_DEFAULT_ONLY_EXT = {"py","ts","tsx","js","jsx","md","txt","toml","yaml","yml","json", ""}


def apply_preset(cfg: Config) -> Config:
    try:
        total_bytes = sum((f.stat().st_size for f in cfg.root.rglob('*') if f.is_file()))
    except Exception:
        total_bytes = 0
    if cfg.preset == "iceberg":
        cfg.respect_gitignore = True
        if not cfg.only_ext:
            cfg.only_ext = set(_DEFAULT_ONLY_EXT)
        cfg.dedup_bits = 16
        cfg.emit_manifest = True
        # Auto-determine mode based on repository size
        if total_bytes < 200_000:
            cfg.llm_mode = "inline"; cfg.budget_tokens = min(cfg.budget_tokens, 6000); cfg.max_file_tokens = 1000
        elif total_bytes < 5_000_000:
            cfg.llm_mode = "summary"; cfg.budget_tokens = min(cfg.budget_tokens, 6000)
        else:
            cfg.llm_mode = "ref"; cfg.budget_tokens = min(cfg.budget_tokens, 4000)
    elif cfg.preset == "raw":
        cfg.llm_mode = "inline"; cfg.dedup_bits = 0; cfg.only_ext = None; cfg.emit_manifest = False
    # pro: maintain user settings
    return cfg


def generate_markdown_report(cfg: Config) -> str:
    cfg = apply_preset(cfg)
    root = cfg.root
    if not root.exists():
        raise FileNotFoundError(f"Path does not exist: {root}")
    if not root.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {root}")

    gitignore = build_gitignore_matcher(root) if cfg.respect_gitignore else None

    def is_ignored(p: Path) -> bool:
        if gitignore and gitignore(str(p.relative_to(root) if p != root else "")):
            return True
        for pat in cfg.exclude_globs:
            if p.match(pat) or any(part == pat for part in p.parts):
                return True
        return False

    def is_omitted(p: Path) -> bool:
        for pat in cfg.omit_globs:
            if p.match(pat) or any(part == pat for part in p.parts):
                return True
        return False

    def is_included(p: Path) -> bool:
        """Check if file matches include patterns (if any are specified)"""
        if not cfg.include_globs:  # No include patterns = include all
            return True
        for pat in cfg.include_globs:
            if p.match(pat) or any(part == pat for part in p.parts):
                return True
        return False

    # Tree & file collection
    tree_lines: list[str] = [str(root)]
    files: list[Path] = []
    stats = Stats()  # Pre-create for accurate directory counting

    def walk(current: Path, prefix: str = "") -> None:
        # Count when entering directory
        stats.total_dirs += 1
        try:
            entries = sorted(list(current.iterdir()), key=lambda x: (not x.is_dir(), x.name.lower()))
        except PermissionError:
            return
        entries = [e for e in entries if not is_ignored(e)]
        for i, child in enumerate(entries):
            last = (i == len(entries)-1)
            joint = "└── " if last else "├── "
            tree_lines.append(f"{prefix}{joint}{child.name}")
            if child.is_dir():
                # Check if it's a symlink and respect follow_symlinks setting
                if child.is_symlink() and not cfg.follow_symlinks:
                    continue  # Skip symlinked directories when follow_symlinks=False
                walk(child, prefix + ("    " if last else "│   "))
            else:
                # For files, add to list (but check symlinks during processing)
                files.append(child)

    walk(root)

    # Generate candidates + deduplication
    candidates: list[dict] = []
    sim_seen: list[int] = []
    for f in files:
        if cfg.only_ext and f.suffix.lstrip(".").lower() not in cfg.only_ext:
            continue
        if is_omitted(f):
            continue
        if not is_included(f):
            continue
        # Skip symlinked files when follow_symlinks=False
        if f.is_symlink() and not cfg.follow_symlinks:
            continue
        try:
            raw = f.read_bytes()
        except Exception:
            continue
        if cfg.max_bytes and len(raw) > cfg.max_bytes:
            raw = raw[: cfg.max_bytes]
        text = raw.decode("utf-8", errors="replace")
        if cfg.masking_mode != "off":
            text = apply_masking(text, mode=cfg.masking_mode)
        sh = simhash64(text)
        # Deduplication
        if cfg.dedup_bits > 0 and any(hamming(sh, h0) <= cfg.dedup_bits for h0 in sim_seen):
            continue
        sim_seen.append(sh)
        candidates.append({
            "path": f,
            "sha256": sha256_bytes(raw),
            "summary": summarize(f, text, max_lines=40),
            "text": text,
            "simhash": sh,
        })

    # Apply budget + reflect mode (Explain & Drift)
    est_total = 0
    selected_blocks: list[tuple[Path, str, str]] = []
    selected_hashes: list[int] = []
    def drift_score_bits(sh: int) -> int:
        if not selected_hashes:
            return 64
        return min((hamming(sh, prev) for prev in selected_hashes), default=64)

    for rec in candidates:
        if cfg.llm_mode == "off":
            break
        sh = rec["simhash"]
        drift_bits = drift_score_bits(sh)
        drift = round(drift_bits / 64, 3)  # 0~1, higher = fresher
        if cfg.llm_mode == "ref":
            meta = json.dumps({"sha256": rec["sha256"], "path": str(rec["path"]), "drift": drift}, ensure_ascii=False)
            tok = estimate_tokens(meta) + 16
            if est_total + tok > cfg.budget_tokens:
                continue
            est_total += tok
            selected_blocks.append((rec["path"], "json", meta))
            selected_hashes.append(sh)
        elif cfg.llm_mode == "summary":
            payload = rec["summary"]
            tok = estimate_tokens(payload)
            if est_total + tok > cfg.budget_tokens:
                continue
            est_total += tok
            text = payload
            if cfg.explain_capsule:
                text += f"\n\n<!-- why: summary; drift={drift} -->"
            selected_blocks.append((rec["path"], "markdown", text))
            selected_hashes.append(sh)
        else:  # inline
            lines = rec["text"].splitlines()
            if cfg.max_lines and len(lines) > cfg.max_lines:
                lines = lines[: cfg.max_lines]
            content = "\n".join(lines)
            if estimate_tokens(content) > cfg.max_file_tokens:
                head = lines[: cfg.sample_head]
                tail = lines[-cfg.sample_tail:] if cfg.sample_tail > 0 else []
                mid = f"\n<!-- [truncated middle: {max(0, len(lines)-len(head)-len(tail))} lines omitted] -->\n"
                content = "\n".join(head + [mid] + tail)
            tok = min(cfg.max_file_tokens, estimate_tokens(content))
            if est_total + tok > cfg.budget_tokens:
                continue
            est_total += tok
            if cfg.explain_capsule:
                content += f"\n\n<!-- why: inline; drift={drift}; tok={tok} -->"
            lang = rec["path"].suffix.lstrip(".") or "text"
            selected_blocks.append((rec["path"], lang, content))
            selected_hashes.append(sh)

    # Final reflection of accumulated statistics
    stats.total_files_in_tree = len(files)
    stats.total_omitted = max(0, len(files) - len(selected_blocks))
    stats.total_with_contents = len(selected_blocks)
    stats.est_tokens_prompt = est_total
    # Note: stats.total_dirs accumulated during walk()

    # Manifest
    if cfg.emit_manifest:
        file_manifest = []
        for (p, lang, t) in selected_blocks:
            entry = {"path": str(p.relative_to(root)), "mode": cfg.llm_mode}
            try:
                # Re-read file for sha256 to ensure it's always present
                entry["sha256"] = sha256_bytes(p.read_bytes())
            except Exception:
                entry["sha256"] = None
            
            if lang == "json":
                try:
                    meta = json.loads(t)
                    entry.update(meta) # drift, etc.
                except Exception:
                    pass
            file_manifest.append(entry)
        
        full_manifest = {
            "stats": {
                "total_dirs": stats.total_dirs,
                "total_files_in_tree": stats.total_files_in_tree,
                "total_omitted": stats.total_omitted,
                "total_with_contents": stats.total_with_contents,
                "est_tokens_prompt": stats.est_tokens_prompt,
            },
            "files": file_manifest
        }
        write_manifest(full_manifest, cfg.output.with_suffix('.manifest.json'))

    return to_markdown(cfg, tree_lines, selected_blocks, stats)
