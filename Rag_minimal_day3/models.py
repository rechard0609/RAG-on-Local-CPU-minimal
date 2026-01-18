from dataclasses import dataclass
from pydantic import BaseModel

# =========================
# Internal Models (Logic)
# =========================

@dataclass
class Document:
    id: int
    text: str


@dataclass
class QueryResult:
    answer: str


# =========================
# API Models (Boundary)
# =========================

class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str
