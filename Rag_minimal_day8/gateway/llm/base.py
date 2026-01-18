from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class LLMResult:
    text: str
    # Some providers return usage (prompt/completion/total tokens)
    usage: Optional[Dict[str, int]] = None


class BaseLLM:
    name: str

    def generate(self, prompt: str, max_tokens: int = 512, temperature: float = 0.2) -> LLMResult:
        raise NotImplementedError
