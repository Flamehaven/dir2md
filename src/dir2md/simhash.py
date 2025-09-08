from __future__ import annotations
from typing import Iterable
import re, hashlib

_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")

def _tokens(s: str) -> list[str]:
    return _TOKEN_RE.findall(s.lower())

def _shingles(seq: list[str], k: int = 4) -> Iterable[int]:
    if k <= 0:
        k = 4
    for i in range(max(0, len(seq)-k+1)):
        payload = " ".join(seq[i:i+k]).encode()
        yield int.from_bytes(hashlib.blake2b(payload, digest_size=8).digest(), 'big')

def simhash64(s: str, k: int = 4) -> int:
    v = [0]*64
    for h in _shingles(_tokens(s), k=k):
        for bit in range(64):
            v[bit] += 1 if (h >> bit) & 1 else -1
    out = 0
    for bit in range(64):
        if v[bit] > 0:
            out |= (1<<bit)
    return out

def hamming(a: int, b: int) -> int:
    return (a ^ b).bit_count()
