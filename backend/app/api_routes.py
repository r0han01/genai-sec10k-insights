# backend/app/api_routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .rag_pipeline import ask_question

router = APIRouter()

# Define input format
class QuestionRequest(BaseModel):
    question: str

# Define output format
class AnswerResponse(BaseModel):
    answer: str
    sources: list[str]

@router.post("/ask", response_model=AnswerResponse)
def ask(request: QuestionRequest):
    try:
        answer, sources = ask_question(request.question)
        source_names = [doc.metadata.get("ticker", "Unknown") for doc in sources]
        return {"answer": answer, "sources": list(set(source_names))}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
