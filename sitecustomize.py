"""Ensure the src/ directory is on sys.path for local runs.

This mirrors the environment when the package is installed, allowing
python -m dir2md and the unit tests to import the package without
requiring pip install -e . first.
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_SRC = _ROOT / "src"

if _SRC.is_dir():
    src_str = str(_SRC)
    if src_str not in sys.path:
        sys.path.insert(0, src_str)
