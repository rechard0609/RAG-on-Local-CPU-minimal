# embedding.py
import numpy as np
import hashlib

def embed(texts):
    vectors = []
    for t in texts:
        h = hashlib.md5(t.encode("utf-8")).hexdigest()
        vec = [int(h[i:i+2], 16) for i in range(0, 32, 2)]
        vectors.append(np.array(vec, dtype=float))
    return vectors
