# reranker.py
class Reranker:
    def rerank(self, query, docs, top_n=2):
        # Mock rerank: 앞에서 top_n
        return docs[:top_n]

def build_reranker(docs):
    return Reranker()
