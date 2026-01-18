# main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pipeline import pipeline

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

@app.post("/chat")
def chat_api(req: ChatRequest):
    result = pipeline(req.query)
    return JSONResponse(
        content={"result": result},
        media_type="application/json; charset=utf-8"
    )
