# models.py
from dataclasses import dataclass
from typing import List

@dataclass
class RetrieveResult:
    candidates: List[str]

@dataclass
class RerankResult:
    contexts: List[str]

@dataclass
class GenerateResult:
    answer: str

@dataclass
class PipelineTrace:
    query: str
    retrieve: RetrieveResult
    rerank: RerankResult
    generate: GenerateResult
