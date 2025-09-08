from __future__ import annotations

def estimate_tokens(text: str) -> int:
    # Simple estimation: 4 chars ≈ 1 token
    return max(1, (len(text) + 3)//4)
