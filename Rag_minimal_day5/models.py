from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class Document:
    id: int
    text: str

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
