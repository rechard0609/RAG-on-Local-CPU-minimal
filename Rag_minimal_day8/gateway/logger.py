from __future__ import annotations

import time
import uuid
from dataclasses import dataclass, asdict
from threading import Lock
from typing import Any, Dict, List


@dataclass
class TraceEvent:
    trace_id: str
    ts: float
    event: str
    data: Dict[str, Any]


class TraceStore:
    """In-memory trace store for learning purposes (not production)."""

    def __init__(self, keep_last: int = 50):
        self.keep_last = keep_last
        self._lock = Lock()
        self._events: List[TraceEvent] = []

    @staticmethod
    def new_trace_id() -> str:
        return uuid.uuid4().hex

    def add(self, trace_id: str, event: str, data: Dict[str, Any] | None = None) -> None:
        if data is None:
            data = {}
        ev = TraceEvent(trace_id=trace_id, ts=time.time(), event=event, data=data)
        with self._lock:
            self._events.append(ev)
            if len(self._events) > self.keep_last:
                self._events = self._events[-self.keep_last :]

    def list_recent(self) -> List[Dict[str, Any]]:
        with self._lock:
            return [asdict(e) for e in self._events]
