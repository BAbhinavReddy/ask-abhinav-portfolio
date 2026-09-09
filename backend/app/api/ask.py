from fastapi import APIRouter, HTTPException

from backend.app.schemas.ask import AskRequest, AskResponse
from backend.app.services.rag_service import retrieve_context
from backend.app.services.ai_service import generate_answer


router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    context = retrieve_context(
        request.question,
        top_k=4,
    )

    if not context:
        raise HTTPException(
            status_code=404,
            detail="No relevant portfolio information found.",
        )

    answer = generate_answer(
        question=request.question,
        context=context,
    )

    return AskResponse(
        answer=answer
    )