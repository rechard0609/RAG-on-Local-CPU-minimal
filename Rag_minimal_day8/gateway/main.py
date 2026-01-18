from __future__ import annotations

import os
import time
from pathlib import Path
from typing import Any, Dict, Optional

import yaml
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from cost import estimate_cost_usd
from logger import TraceStore
from metrics import Metrics
from router import build_llm
from usage import Usage, approx_tokens


CONFIG_PATH = Path(os.environ.get("CONFIG_PATH", "/app/config.yaml"))


def load_config() -> Dict[str, Any]:
    if not CONFIG_PATH.exists():
        raise RuntimeError(f"config.yaml not found: {CONFIG_PATH}")
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


cfg = load_config()
trace_store = TraceStore(keep_last=int((cfg.get("monitoring") or {}).get("traces_keep_last", 50)))
metrics = Metrics()
pricing = cfg.get("pricing_per_1k_tokens_usd") or {}

gateway_cfg = cfg.get("gateway") or {}
timeout_seconds = int(gateway_cfg.get("timeout_seconds", 60))

app = FastAPI(title="Day8 LLM Gateway (Minimal)")

allowed_origins = gateway_cfg.get("cors_allow_origins") or ["http://localhost:3000", "http://127.0.0.1:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    model: Optional[str] = Field(default=None, description="Provider name: openai|gemini|claude|solar|local")
    max_tokens: int = Field(default=512, ge=1, le=4096)
    temperature: float = Field(default=0.2, ge=0.0, le=2.0)


class QueryResponse(BaseModel):
    trace_id: str
    model: str
    answer: str
    latency_ms: float
    usage: Dict[str, Any]


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/status")
def status():
    return metrics.to_dict()


@app.get("/traces")
def traces():
    return {"events": trace_store.list_recent()}


@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest):
    # Reload config on each request (simple, for learning)
    # If you want a static config, load once.
    global cfg, pricing, timeout_seconds
    cfg = load_config()
    pricing = cfg.get("pricing_per_1k_tokens_usd") or {}
    gateway_cfg = cfg.get("gateway") or {}
    timeout_seconds = int(gateway_cfg.get("timeout_seconds", 60))

    provider = req.model or (cfg.get("llm") or {}).get("default") or "solar"
    trace_id = TraceStore.new_trace_id()
    trace_store.add(trace_id, "request", {"model": provider})

    start = time.perf_counter()
    try:
        llm = build_llm(provider, cfg)
        result = llm.generate(req.prompt, max_tokens=req.max_tokens, temperature=req.temperature)
    except Exception as e:
        trace_store.add(trace_id, "error", {"message": str(e)})
        raise HTTPException(status_code=400, detail=str(e))

    latency_ms = round((time.perf_counter() - start) * 1000.0, 2)

    # Token usage
    prompt_tokens = 0
    completion_tokens = 0
    total_tokens = 0

    if result.usage:
        prompt_tokens = int(result.usage.get("prompt_tokens", 0))
        completion_tokens = int(result.usage.get("completion_tokens", 0))
        total_tokens = int(result.usage.get("total_tokens", prompt_tokens + completion_tokens))
    else:
        prompt_tokens = approx_tokens(req.prompt)
        completion_tokens = approx_tokens(result.text)
        total_tokens = prompt_tokens + completion_tokens

    cost_usd = estimate_cost_usd(pricing, provider, total_tokens)

    usage = Usage(
        model=provider,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        total_tokens=total_tokens,
        cost_usd=cost_usd,
    )

    metrics.record(model=provider, latency_ms=latency_ms, tokens=total_tokens)
    trace_store.add(trace_id, "response", {"latency_ms": latency_ms, "total_tokens": total_tokens, "cost_usd": cost_usd})

    return QueryResponse(
        trace_id=trace_id,
        model=provider,
        answer=result.text,
        latency_ms=latency_ms,
        usage=usage.to_dict(),
    )
