from __future__ import annotations
import argparse, zipfile, hashlib, os, json
from pathlib import Path
from typing import Any

try:
    import tomllib as _toml_loader
except ModuleNotFoundError:
    try:
        import tomli as _toml_loader
    except ModuleNotFoundError:
        _toml_loader = None

from .core import Config, generate_markdown_report
from . import __version__

# Load .env file if it exists (for Pro license and configuration)
def load_env_file():
    current = Path.cwd()
    for parent in [current] + list(current.parents):
        env_file = parent / '.env'
        if env_file.exists():
            try:
                for line in env_file.read_text(encoding='utf-8').splitlines():
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        os.environ[key.strip()] = value.strip()
                break
            except Exception:
                pass

load_env_file()

DEFAULT_OUTPUT = "PROJECT_BLUEPRINT.md"
DEFAULT_EXCLUDES = [
    ".git",
    "__pycache__",
    "node_modules",
    ".venv",
    "build",
    "dist",
    "*.pyc",
    ".DS_Store",
    ".env",
    ".env.*",
    "*.env",
    "*.pem",
    "*.key",
    "*.p12",
    "*.pfx",
    "*.cer",
    "*.crt",
]
_CONFIG_KEYS = {
    "path",
    "output",
    "preset",
    "llm_mode",
    "budget_tokens",
    "max_file_tokens",
    "dedup",
    "sample_head",
    "sample_tail",
    "explain",
    "include_glob",
    "exclude_glob",
    "omit_glob",
    "only_ext",
    "respect_gitignore",
    "follow_symlinks",
    "max_bytes",
    "max_lines",
    "emit_manifest",
    "stats",
    "capsule",
    "dry_run",
    "no_timestamp",
    "masking",
    "mask_patterns",
    "mask_pattern_files",
}


def positive_int(v: str) -> int:
    try:
        iv = int(v)
    except ValueError:
        raise argparse.ArgumentTypeError("Please enter an integer value.")
    if iv <= 0:
        raise argparse.ArgumentTypeError("Only positive integers are allowed.")
    return iv


def _load_pyproject_config() -> dict[str, Any]:
    if _toml_loader is None:
        return {}

    decode_error = getattr(_toml_loader, "TOMLDecodeError", ValueError)
    current_dir = Path.cwd()
    for path in [current_dir] + list(current_dir.parents):
        pyproject_path = path / "pyproject.toml"
        if not pyproject_path.is_file():
            continue
        try:
            with pyproject_path.open("rb") as handle:
                data = _toml_loader.load(handle)
        except (decode_error, OSError):
            return {}

        tool_config = data.get("tool", {}).get("dir2md")
        if not isinstance(tool_config, dict):
            return {}

        sanitized: dict[str, Any] = {}
        for raw_key, value in tool_config.items():
            key = raw_key.replace('-', '_')
            if key not in _CONFIG_KEYS:
                if raw_key == "masking" and isinstance(value, dict):
                    patterns = value.get("patterns")
                    if patterns:
                        sanitized.setdefault("mask_patterns", [])
                        if isinstance(patterns, list):
                            sanitized["mask_patterns"].extend(str(item) for item in patterns)
                        else:
                            sanitized["mask_patterns"].append(str(patterns))
                    pattern_files = value.get("pattern_files")
                    if pattern_files:
                        sanitized.setdefault("mask_pattern_files", [])
                        if isinstance(pattern_files, list):
                            sanitized["mask_pattern_files"].extend(str(item) for item in pattern_files)
                        else:
                            sanitized["mask_pattern_files"].append(str(pattern_files))
                continue
            if key in {"include_glob", "exclude_glob", "omit_glob", "mask_patterns"}:
                if value is None:
                    continue
                if isinstance(value, list):
                    sanitized[key] = [str(item) for item in value]
                else:
                    sanitized[key] = [str(value)]
                continue
            if key == "mask_pattern_files":
                if value is None:
                    continue
                if isinstance(value, list):
                    sanitized[key] = [str(item) for item in value]
                else:
                    sanitized[key] = [str(value)]
                continue
            if key == "only_ext":
                if value is None:
                    continue
                if isinstance(value, list):
                    sanitized[key] = ",".join(str(item) for item in value)
                else:
                    sanitized[key] = str(value)
                continue
            if key in {"budget_tokens", "max_file_tokens", "dedup", "sample_head", "sample_tail", "max_bytes", "max_lines"}:
                try:
                    sanitized[key] = int(value)
                except (TypeError, ValueError):
                    continue
                continue
            if key in {"respect_gitignore", "follow_symlinks", "emit_manifest", "stats", "capsule", "dry_run", "no_timestamp", "explain"}:
                sanitized[key] = bool(value)
                continue
            sanitized[key] = value
        return sanitized
    return {}


def _load_patterns_from_file(source: str) -> list[str]:
    """Load regex patterns from a file or file:// URI."""
    raw = source
    if raw.startswith("file://"):
        raw = raw[7:]
        # Handle Windows absolute paths: file:///C:/path -> C:/path
        if raw.startswith("/") and len(raw) > 2 and raw[2] == ":":
            raw = raw[1:]
    path = Path(raw)
    patterns: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"[WARN] Could not read mask pattern file {source!r}: {exc}")
        return patterns
    text = text.strip()
    if not text:
        return patterns
    if path.suffix.lower() in {".json", ".jsonc"}:
        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            print(f"[WARN] Could not parse JSON mask pattern file {source!r}: {exc}")
            return patterns
        if isinstance(data, list):
            patterns.extend(str(item) for item in data)
        elif isinstance(data, dict):
            items = data.get("patterns")
            if isinstance(items, list):
                patterns.extend(str(item) for item in items)
            elif items:
                patterns.append(str(items))
    else:
        for line in text.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                patterns.append(line)
    return patterns


def _resolve_custom_mask_patterns(explicit: list[str] | None, files: list[str] | None) -> list[str]:
    combined: list[str] = []
    seen: set[str] = set()
    for pattern in explicit or []:
        if pattern and pattern not in seen:
            seen.add(pattern)
            combined.append(pattern)
    for source in files or []:
        for pattern in _load_patterns_from_file(source):
            if pattern and pattern not in seen:
                seen.add(pattern)
                combined.append(pattern)
    return combined


def main(argv: list[str] | None = None) -> int:
    config_from_file = _load_pyproject_config()

    ap = argparse.ArgumentParser(prog="dir2md", description="Directory -> Markdown exporter with LLM optimization")
    ap.add_argument("path", nargs="?", default=".")
    ap.add_argument("-o", "--output")

    ap.add_argument("--preset", choices=["iceberg", "pro", "raw"], help="Preset mode: iceberg/pro/raw")

    ap.add_argument("--llm-mode", choices=["off", "ref", "summary", "inline"])
    ap.add_argument("--budget-tokens", type=int)
    ap.add_argument("--max-file-tokens", type=int)
    ap.add_argument("--dedup", type=int)
    ap.add_argument("--sample-head", type=int)
    ap.add_argument("--sample-tail", type=int)
    ap.add_argument("--explain", action="store_true", help="Include selection rationale and drift_score in capsule comments")

    ap.add_argument("--include-glob", action="append", help="Gitignore-style include pattern (gitwildmatch syntax)")
    ap.add_argument("--exclude-glob", action="append", help="Gitignore-style exclude pattern")
    ap.add_argument("--omit-glob", action="append", help="Gitignore-style omit pattern (skips content)")
    ap.add_argument("--only-ext", help="Comma-separated extension list (e.g. py,md)")
    ap.add_argument("--respect-gitignore", action="store_true")
    ap.add_argument("--follow-symlinks", action="store_true")
    ap.add_argument("--max-bytes", type=positive_int)
    ap.add_argument("--max-lines", type=positive_int)

    ap.add_argument("--emit-manifest", action="store_true", help="Write JSON manifest (raw preset overrides to off)")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--capsule", action="store_true", help="Package md+manifest into zip")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-timestamp", action="store_true", help="Omit timestamp for reproducible output")
    ap.add_argument("--masking", choices=["off", "basic", "advanced"], help="Secret masking mode (default: basic, advanced requires Pro license)")
    ap.add_argument("--mask-pattern", action="append", dest="mask_patterns", help="Additional custom regex patterns to mask (applies alongside built-in rules)")
    ap.add_argument("--mask-pattern-file", action="append", dest="mask_pattern_files", help="Load custom mask regex patterns from file (JSON array or newline separated list). Supports file:// URIs.")

    ap.add_argument("-V", "--version", action="version", version=f"dir2md {__version__}")

    if config_from_file:
        ap.set_defaults(**config_from_file)

    ns = ap.parse_args(argv)

    root = Path(ns.path).resolve()

    if ns.output:
        output = Path(ns.output)
    else:
        if root.is_dir():
            output = root / f"{root.name}.md"
        else:
            output = Path(DEFAULT_OUTPUT).resolve()
    only_ext = {e.strip().lstrip('.') for e in (ns.only_ext or "").split(',') if e.strip()} or None

    cfg = Config(
        root=root,
        output=output,
        include_globs=list(ns.include_glob or []),
        exclude_globs=list(ns.exclude_glob or []) + DEFAULT_EXCLUDES,
        omit_globs=list(ns.omit_glob or []),
        respect_gitignore=bool(ns.respect_gitignore or False),
        follow_symlinks=bool(ns.follow_symlinks or False),
        max_bytes=int(ns.max_bytes) if ns.max_bytes is not None else 200_000,
        max_lines=int(ns.max_lines) if ns.max_lines is not None else 2000,
        include_contents=True,
        only_ext=only_ext,
        add_stats=bool(ns.stats or False),
        add_toc=False,
        llm_mode=(ns.llm_mode or "ref"),
        budget_tokens=int(ns.budget_tokens) if ns.budget_tokens is not None else 6000,
        max_file_tokens=int(ns.max_file_tokens) if ns.max_file_tokens is not None else 1200,
        dedup_bits=int(ns.dedup) if ns.dedup is not None else 16,
        sample_head=int(ns.sample_head) if ns.sample_head is not None else 120,
        sample_tail=int(ns.sample_tail) if ns.sample_tail is not None else 40,
        strip_comments=False,
        emit_manifest=bool(ns.emit_manifest if ns.emit_manifest is not None else True),
        preset=str(ns.preset or "pro"),
        explain_capsule=bool(ns.explain or False),
        no_timestamp=bool(ns.no_timestamp or False),
        masking_mode=str(ns.masking or "basic"),
        custom_mask_patterns=_resolve_custom_mask_patterns(
            list(ns.mask_patterns or []),
            list(ns.mask_pattern_files or []),
        ),
    )

    md = generate_markdown_report(cfg)

    if ns.dry_run:
        h = hashlib.sha256(md.encode('utf-8')).hexdigest()[:10]
        print(f"[dry-run] preset={cfg.preset} mode={cfg.llm_mode} est_tokens~{cfg.budget_tokens} md={h}")
        return 0

    output.write_text(md, encoding="utf-8")
    if ns.capsule:
        with zipfile.ZipFile(output.with_suffix('.capsule.zip'), 'w') as z:
            z.write(output)
            if cfg.emit_manifest and output.with_suffix('.manifest.json').exists():
                z.write(output.with_suffix('.manifest.json'))
    try:
        print(f"[dir2md] Wrote: {output}")
    except UnicodeEncodeError:
        print("[dir2md] Wrote: (File path contains unprintable characters, but the file was likely created successfully)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



