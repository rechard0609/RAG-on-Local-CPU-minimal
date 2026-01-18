# keyword_index.py
from collections import Counter

class KeywordIndex:
    def __init__(self, docs):
        self.docs = docs
        self.tokens = [Counter(d.text.split()) for d in docs]

    def search(self, query: str, top_k: int):
        q_tokens = query.split()
        scores = []
        for i, doc in enumerate(self.docs):
            score = sum(self.tokens[i].get(t, 0) for t in q_tokens)
            scores.append((score, doc.text))

        scores.sort(reverse=True)
        return [t for s, t in scores[:top_k] if s > 0]
