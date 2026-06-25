from fastapi import APIRouter

from src.api.schemas import (
    QuestionRequest,
    AnswerResponse
)

from src.rag.rag_pipeline import ask_appx

router = APIRouter()


@router.post(
    "/ask",
    response_model=AnswerResponse
)
def ask_question(
    request: QuestionRequest
):

    answer = ask_appx(
        request.question
    )

    return AnswerResponse(
        question=request.question,
        answer=answer
    )