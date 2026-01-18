# vectorstore.py
import numpy as np

class VectorStore:
    def __init__(self, vectors, texts):
        self.vectors = np.array(vectors)
        self.texts = texts

    def search(self, query_vec, top_k: int):
        scores = self.vectors @ query_vec
        idx = scores.argsort()[::-1][:top_k]
        return [self.texts[i] for i in idx]

def build_store(docs):
    from embedding import embed
    texts = [d.text for d in docs]
    vectors = embed(texts)
    return VectorStore(vectors, texts)
