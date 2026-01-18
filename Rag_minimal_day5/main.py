from fastapi import FastAPI
from pipeline import pipeline
from models import QueryRequest, QueryResponse

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query", response_model=QueryResponse)
def query_api(req: QueryRequest):
    answer = pipeline(req.query)
    return QueryResponse(answer=answer)
