from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pipeline import pipeline
import json

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

@app.post("/chat")
def chat_api(req: ChatRequest):
    result = pipeline(req.query)

    # ensure_ascii=False 가 핵심
    return JSONResponse(
        content=json.loads(
            json.dumps({"result": result}, ensure_ascii=False)
        ),
        media_type="application/json; charset=utf-8"
    )
