from __future__ import annotations
from pathlib import Path
import ast

def summarize(path: Path, content: str, max_lines: int = 60) -> str:
    ext = path.suffix.lower()
    if ext == ".py":
        try:
            tree = ast.parse(content)
            funcs = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
            clss  = [n.name for n in tree.body if isinstance(n, ast.ClassDef)]
            imps  = []
            for n in tree.body:
                if isinstance(n, ast.Import):
                    imps.extend([a.name for a in n.names])
                if isinstance(n, ast.ImportFrom):
                    imps.extend([a.name for a in n.names])
            lines = []
            if imps:  lines.append(f"- imports: {', '.join(imps)[:200]}")
            if clss:  lines.append(f"- classes: {', '.join(clss)[:200]}")
            if funcs: lines.append(f"- functions: {', '.join(funcs)[:200]}")
            return "\n".join(lines) or "- (no symbols)"
        except Exception:
            pass
    if ext in {".md", ".markdown"}:
        heads = [ln.strip() for ln in content.splitlines() if ln.strip().startswith("#")][:10]
        return "\n".join([f"- {h}" for h in heads]) or _first_lines(content, max_lines)
    return _first_lines(content, max_lines)

def _first_lines(content: str, max_lines: int) -> str:
    lines = content.splitlines()[:max_lines]
    return "\n".join([f"- {ln}" for ln in lines if ln.strip()])
