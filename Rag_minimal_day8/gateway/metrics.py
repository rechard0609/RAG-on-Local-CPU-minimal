from __future__ import annotations

import time
from dataclasses import dataclass
from threading import Lock
from typing import Dict, Optional


@dataclass
class MetricsSnapshot:
    requests_total: int
    avg_latency_ms: float
    last_model: Optional[str]
    last_request_ts: Optional[float]
    tokens_total: int


class Metrics:
    """In-memory metrics (learning-only)."""

    def __init__(self):
        self._lock = Lock()
        self._requests_total = 0
        self._latency_sum_ms = 0.0
        self._last_model: Optional[str] = None
        self._last_request_ts: Optional[float] = None
        self._tokens_total = 0

    def record(self, model: str, latency_ms: float, tokens: int) -> None:
        with self._lock:
            self._requests_total += 1
            self._latency_sum_ms += float(latency_ms)
            self._last_model = model
            self._last_request_ts = time.time()
            self._tokens_total += int(tokens)

    def snapshot(self) -> MetricsSnapshot:
        with self._lock:
            avg = (self._latency_sum_ms / self._requests_total) if self._requests_total else 0.0
            return MetricsSnapshot(
                requests_total=self._requests_total,
                avg_latency_ms=round(avg, 2),
                last_model=self._last_model,
                last_request_ts=self._last_request_ts,
                tokens_total=self._tokens_total,
            )

    def to_dict(self) -> Dict:
        snap = self.snapshot()
        return {
            "requests_total": snap.requests_total,
            "avg_latency_ms": snap.avg_latency_ms,
            "last_model": snap.last_model,
            "last_request_ts": snap.last_request_ts,
            "tokens_total": snap.tokens_total,
        }
