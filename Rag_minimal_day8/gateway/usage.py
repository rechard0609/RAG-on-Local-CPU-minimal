from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Optional


@dataclass
class Usage:
    model: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    cost_usd: float

    def to_dict(self) -> Dict:
        return asdict(self)


def approx_tokens(text: str) -> int:
    """Rough token estimator for learning (≈ 4 chars/token)."""
    if not text:
        return 0
    return max(1, len(text) // 4)
