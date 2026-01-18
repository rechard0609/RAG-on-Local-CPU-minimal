# pipeline.py
from orchestration import run_pipeline

def pipeline(query: str):
    trace = run_pipeline(query)
    return {
        "query": trace.query,
        "candidates": trace.retrieve.candidates,
        "contexts": trace.rerank.contexts,
        "answer": trace.generate.answer,
    }
