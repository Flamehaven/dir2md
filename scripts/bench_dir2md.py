from __future__ import annotations
import time, json, argparse
from pathlib import Path
from dir2md.core import Config, generate_markdown_report

def run_case(root: Path, preset: str, mode: str | None, budget: int, file_budget: int) -> dict:
    cfg = Config(
        root=root, output=root/"_BENCH.md", include_globs=[], exclude_globs=[], omit_globs=[],
        respect_gitignore=True, follow_symlinks=False, max_bytes=200_000, max_lines=2000,
        include_contents=True, only_ext=None, add_stats=True, add_toc=False,
        llm_mode=(mode or "ref"), budget_tokens=budget, max_file_tokens=file_budget,
        dedup_bits=16, sample_head=120, sample_tail=40, strip_comments=False,
        emit_manifest=False, preset=preset, explain_capsule=True,
    )
    t0 = time.perf_counter()
    md = generate_markdown_report(cfg)
    dt = time.perf_counter() - t0
    est = md.split("Estimated tokens (prompt): `")[-1].split("`")[0]
    return {"preset": preset, "mode": cfg.llm_mode, "elapsed_sec": round(dt,3), "est_tokens": int(est)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=".")
    ns = ap.parse_args()
    root = Path(ns.path).resolve()
    cases = [
        ("iceberg", None, 6000, 1000),
        ("pro", "summary", 6000, 1000),
        ("pro", "ref", 4000, 1000),
        ("pro", "inline", 8000, 1200),
    ]
    rows = [run_case(root, *c) for c in cases]
    print(json.dumps(rows, indent=2))

if __name__ == "__main__":
    main()
