from __future__ import annotations
from pathlib import Path
import json, hashlib

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def write_manifest(data: dict, out: Path) -> None:
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
