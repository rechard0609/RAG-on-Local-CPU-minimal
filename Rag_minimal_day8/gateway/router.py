from __future__ import annotations

from typing import Any, Dict

from llm.base import BaseLLM
from llm.openai_llm import OpenAILLM
from llm.gemini_llm import GeminiLLM
from llm.claude_llm import ClaudeLLM
from llm.solar_llm import SolarLLM
from llm.local_llm import LocalLLM


def build_llm(provider_name: str, cfg: Dict[str, Any]) -> BaseLLM:
    providers = (cfg.get("llm") or {}).get("providers") or {}
    p = providers.get(provider_name)
    if not p:
        raise ValueError(f"Unknown provider: {provider_name}")

    if provider_name == "openai":
        return OpenAILLM(model=p.get("model", "gpt-4o-mini"))
    if provider_name == "gemini":
        return GeminiLLM(model=p.get("model", "gemini-1.5-flash"))
    if provider_name == "claude":
        return ClaudeLLM(model=p.get("model", "claude-3-sonnet"))
    if provider_name == "solar":
        return SolarLLM(model=p.get("model", "solar-10.7b"), base_url=p.get("base_url", "https://api.upstage.ai/v1"))
    if provider_name == "local":
        return LocalLLM(endpoint=p.get("endpoint", "http://local-llm:8080"))

    raise ValueError(f"Unsupported provider: {provider_name}")
