# reranker.py
from config import ALPHA, BETA

class Reranker:
    def __init__(self, docs):
        self.docs = docs

    def rerank(self, query, candidates, vector_scores, keyword_scores, top_n):
        fused = {}
        for c in candidates:
            v = vector_scores.get(c, 0.0)
            k = keyword_scores.get(c, 0.0)
            fused[c] = ALPHA * v + BETA * k

        ranked = sorted(fused.items(), key=lambda x: x[1], reverse=True)
        return [t for t, _ in ranked[:top_n]]

def build_reranker(docs):
    return Reranker(docs)
