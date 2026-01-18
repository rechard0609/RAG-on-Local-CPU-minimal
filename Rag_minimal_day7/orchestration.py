# orchestration.py
from ingest import build_assets
from embedding import embed
from models import RetrieveResult, RerankResult, GenerateResult, PipelineTrace
from llm import generate
from config import VECTOR_TOP_K, KEYWORD_TOP_K, RERANK_TOP_N

_store = None
_keyword = None
_reranker = None

def get_assets():
    global _store, _keyword, _reranker
    if _store is None:
        _store, _keyword, _reranker = build_assets()
    return _store, _keyword, _reranker

def step_retrieve(query: str) -> RetrieveResult:
    store, keyword, _ = get_assets()

    qvec = embed([query])[0]
    vector_candidates = store.search(qvec, VECTOR_TOP_K)
    keyword_candidates = keyword.search(query, KEYWORD_TOP_K)

    merged = list(dict.fromkeys(vector_candidates + keyword_candidates))
    print("CANDIDATES:", merged)

    return RetrieveResult(candidates=merged)

def step_rerank(query: str, r: RetrieveResult) -> RerankResult:
    store, keyword, reranker = get_assets()

    vector_scores = {}
    qvec = embed([query])[0]
    for c in r.candidates:
        vector_scores[c] = qvec @ embed([c])[0]

    keyword_scores = {}
    for c in r.candidates:
        keyword_scores[c] = sum(1 for t in query.split() if t in c)

    contexts = reranker.rerank(
        query,
        r.candidates,
        vector_scores,
        keyword_scores,
        RERANK_TOP_N
    )

    print("RERANKED:", contexts)
    return RerankResult(contexts=contexts)

def step_generate(query: str, rr: RerankResult) -> GenerateResult:
    context = "\n".join(rr.contexts)
    prompt = f"""
문서:
{context}

질문:
{query}
"""
    return GenerateResult(answer=generate(prompt))

def run_pipeline(query: str) -> PipelineTrace:
    r = step_retrieve(query)
    rr = step_rerank(query, r)
    g = step_generate(query, rr)

    return PipelineTrace(
        query=query,
        retrieve=r,
        rerank=rr,
        generate=g
    )
