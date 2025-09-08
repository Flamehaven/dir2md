from __future__ import annotations
import argparse, zipfile, hashlib
from pathlib import Path
from .core import Config, generate_markdown_report
from . import __version__

DEFAULT_EXCLUDES = [
    ".git", "__pycache__", "node_modules", ".venv",
    "build", "dist", "*.pyc", ".DS_Store",
]

def positive_int(v: str) -> int:
    try:
        iv = int(v)
    except ValueError:
        raise argparse.ArgumentTypeError("Please enter an integer value.")
    if iv <= 0:
        raise argparse.ArgumentTypeError("Only positive integers are allowed.")
    return iv

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="dir2md", description="Directory → Markdown exporter with LLM optimization")
    ap.add_argument("path", nargs="?", default=".")
    ap.add_argument("-o", "--output", default="PROJECT_BLUEPRINT.md")

    # Preset options
    ap.add_argument("--preset", default="raw", choices=["iceberg","pro","raw"], help="Preset mode: iceberg/pro/raw")

    # Token and selection control
    ap.add_argument("--llm-mode", choices=["off","ref","summary","inline"], default=None)
    ap.add_argument("--budget-tokens", type=int, default=6000)
    ap.add_argument("--max-file-tokens", type=int, default=1200)
    ap.add_argument("--dedup", type=int, default=16)
    ap.add_argument("--sample-head", type=int, default=120)
    ap.add_argument("--sample-tail", type=int, default=40)
    ap.add_argument("--explain", action="store_true", help="Include selection rationale and drift_score in capsule comments")

    # Filtering and safety controls
    ap.add_argument("--include-glob", action="append", default=[])
    ap.add_argument("--exclude-glob", action="append", default=[])
    ap.add_argument("--omit-glob", action="append", default=[])
    ap.add_argument("--only-ext", default="")
    ap.add_argument("--respect-gitignore", action="store_true")
    ap.add_argument("--follow-symlinks", action="store_true")
    ap.add_argument("--max-bytes", type=positive_int, default=200_000)
    ap.add_argument("--max-lines", type=positive_int, default=2000)

    # Output options
    ap.add_argument("--emit-manifest", action="store_true")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--capsule", action="store_true", help="Package md+manifest into zip")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-timestamp", action="store_true", help="Omit timestamp for reproducible output")
    ap.add_argument("--masking", choices=["off", "basic", "advanced"], default="off", help="Secret masking mode (advanced requires Pro license)")

    ap.add_argument("-V", "--version", action="version", version=f"dir2md {__version__}")

    ns = ap.parse_args(argv)

    root = Path(ns.path).resolve()
    output = Path(ns.output)
    only_ext = {e.strip().lstrip('.') for e in ns.only_ext.split(',') if e.strip()} or None

    cfg = Config(
        root=root,
        output=output,
        include_globs=list(ns.include_glob),
        exclude_globs=list(ns.exclude_glob or DEFAULT_EXCLUDES),
        omit_globs=list(ns.omit_glob),
        respect_gitignore=bool(ns.respect_gitignore),
        follow_symlinks=bool(ns.follow_symlinks),
        max_bytes=int(ns.max_bytes) if ns.max_bytes else None,
        max_lines=int(ns.max_lines) if ns.max_lines else None,
        include_contents=True,
        only_ext=only_ext,
        add_stats=bool(ns.stats or True),
        add_toc=False,
        llm_mode=(ns.llm_mode or "ref"),
        budget_tokens=int(ns.budget_tokens),
        max_file_tokens=int(ns.max_file_tokens),
        dedup_bits=int(ns.dedup),
        sample_head=int(ns.sample_head),
        sample_tail=int(ns.sample_tail),
        strip_comments=False,
        emit_manifest=bool(ns.emit_manifest),
        preset=str(ns.preset),
        explain_capsule=bool(ns.explain),
        no_timestamp=bool(ns.no_timestamp),
        masking_mode=str(ns.masking),
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
    print(f"[dir2md] Wrote: {output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
