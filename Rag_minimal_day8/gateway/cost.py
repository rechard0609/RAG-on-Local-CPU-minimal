from __future__ import annotations

from typing import Dict


def estimate_cost_usd(pricing_per_1k: Dict[str, float], model: str, total_tokens: int) -> float:
    rate = float(pricing_per_1k.get(model, 0.0))
    return round((total_tokens / 1000.0) * rate, 6)
