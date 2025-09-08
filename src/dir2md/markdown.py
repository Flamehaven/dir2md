from __future__ import annotations
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .core import Config, Stats

def to_markdown(cfg: 'Config', tree_lines: list[str], file_blocks: list[tuple[Path, str, str]], stats: 'Stats') -> str:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parts: list[str] = []
    parts.append("# Project Blueprint\n")
    parts.append(f"- Root: `{cfg.root}`  ")
    if not cfg.no_timestamp:
        parts.append(f"- Generated: `{ts}`  ")
    parts.append(f"- Preset: `{cfg.preset}`  ")
    parts.append(f"- LLM mode: `{cfg.llm_mode}`  ")
    parts.append(f"- Estimated tokens (prompt): `{stats.est_tokens_prompt}`  ")
    parts.append("")
    parts.append("## Directory Tree\n")
    parts.append("```\n" + "\n".join(tree_lines) + "\n````\n\n")
    if cfg.llm_mode != "off" and file_blocks:
        parts.append("## File Contents\n")
        for path, lang, text in file_blocks:
            rel = path.relative_to(cfg.root)
            parts.append(f"### File: `{rel}`\n")
            parts.append(f"```{lang}\n{text}\n\n````\n")
    if cfg.add_stats:
        parts.append("## Summary\n")
        parts.append("| metric | value |\n|---|---:|")
        parts.append(f"| dirs | {stats.total_dirs} |")
        parts.append(f"| files in tree | {stats.total_files_in_tree} |")
        parts.append(f"| selected files | {stats.total_with_contents} |")
        parts.append(f"| omitted | {stats.total_omitted} |")
        parts.append(f"| est tokens (prompt) | {stats.est_tokens_prompt} |\n")
    return "\n".join(parts)