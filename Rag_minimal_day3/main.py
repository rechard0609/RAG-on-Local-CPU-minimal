from fastapi import FastAPI
from pipeline import pipeline
from models import QueryRequest, QueryResponse

app = FastAPI(
    title="RAG Minimal API",
    description="Day 3 - RAG를 서비스로 만드는 최소 구조",
    version="0.1.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query", response_model=QueryResponse)
def query_api(req: QueryRequest):
    answer = pipeline(req.query)
    return QueryResponse(answer=answer)
