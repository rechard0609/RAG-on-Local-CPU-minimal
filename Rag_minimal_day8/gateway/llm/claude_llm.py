from __future__ import annotations

import requests

from .base import BaseLLM, LLMResult
from settings import API_KEYS  # ← 수정!


class ClaudeLLM(BaseLLM):
    name = "claude"

    def __init__(self, model: str):
        self.model = model
        self.api_key = (
            API_KEYS.get("claude", {})
            .get("api_key", "")
            .strip()
        )

    def generate(
        self,
        prompt: str,
        max_tokens: int = 512,
        temperature: float = 0.2
    ) -> LLMResult:
        if not self.api_key:
            raise RuntimeError("CLAUDE_API_KEY is not set")

        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }
        payload = {
            "model": self.model,
            "max_tokens": int(max_tokens),
            "temperature": float(temperature),
            "messages": [
                {"role": "user", "content": prompt}
            ],
        }

        r = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=60
        )
        if r.status_code >= 400:
            raise RuntimeError(
                f"Anthropic API error {r.status_code}: {r.text}"
            )

        data = r.json()

        # content is a list of blocks
        text = ""
        try:
            blocks = data.get("content") or []
            text = "".join(
                b.get("text", "")
                for b in blocks
                if b.get("type") == "text"
            )
        except Exception:
            text = str(data)

        usage = data.get("usage") or {}
        input_tokens = int(usage.get("input_tokens", 0))
        output_tokens = int(usage.get("output_tokens", 0))

        return LLMResult(
            text=text,
            usage={
                "prompt_tokens": input_tokens,
                "completion_tokens": output_tokens,
                "total_tokens": input_tokens + output_tokens,
            },
        )
