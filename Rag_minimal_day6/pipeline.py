# pipeline.py
from ingest import build_assets
from config import TOP_K, TOP_N
from llm import generate_answer

_store = None
_reranker = None

def get_assets():
    global _store, _reranker
    if _store is None or _reranker is None:
        _store, _reranker = build_assets()
    return _store, _reranker

def pipeline(query: str):
    store, reranker = get_assets()

    candidates = store.search(query, top_k=TOP_K)
    print("CANDIDATES:", candidates)

    contexts = reranker.rerank(query, candidates, top_n=TOP_N)
    print("RERANKED:", contexts)

    answer = generate_answer(query, contexts)

    return {
        "query": query,
        "candidates": candidates,
        "contexts": contexts,
        "answer": answer,
    }
