# embedding.py
import numpy as np

def embed(texts: list[str]) -> list[list[float]]:
    vectors = []
    for t in texts:
        # 매우 단순한 Mock Embedding (길이 기반)
        vectors.append([len(t) % 10, len(t) % 7, len(t) % 5])
    return vectors
