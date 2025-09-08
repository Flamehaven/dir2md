from __future__ import annotations
from pathlib import Path
from typing import List, Optional, Callable

try:
    from pathspec import PathSpec
except Exception:
    PathSpec = None  # type: ignore


def _collect_gitignore_lines(root: Path) -> List[str]:
    lines: List[str] = []
    for gi in root.rglob('.gitignore'):
        rel_dir = gi.parent.relative_to(root)
        base = str(rel_dir).replace('\\', '/')
        raw = gi.read_text(encoding='utf-8', errors='ignore').splitlines()
        for ln in raw:
            s = ln.strip()
            if not s or s.startswith('#'):
                continue
            if s.startswith('/'):
                s = s[1:]
            if base and s:
                s = f"{base}/{s}"
            lines.append(s)
    return lines


def build_gitignore_matcher(root: Path) -> Optional[Callable[[str], bool]]:
    if PathSpec is None:
        return None
    lines = _collect_gitignore_lines(root)
    top = root / ".gitignore"
    if top.exists():
        lines = top.read_text(encoding='utf-8', errors='ignore').splitlines() + lines
    if not lines:
        return None
    spec = PathSpec.from_lines("gitwildmatch", lines)
    def match(relpath: str) -> bool:
        return spec.match_file(relpath)
    return match