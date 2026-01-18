# vectorstore.py
import numpy as np

class VectorStore:
    def __init__(self, vectors, texts):
        self.vectors = np.array(vectors)
        self.texts = texts

    def search(self, query, top_k=3):
        # Mock search: 앞에서 top_k 반환
        return self.texts[:top_k]

def build_store(docs):
    texts = [d.text for d in docs]
    vectors = [[len(t) % 10, len(t) % 7, len(t) % 5] for t in texts]
    return VectorStore(vectors, texts)
