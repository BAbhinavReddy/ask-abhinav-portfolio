from backend.app.services.rag_service import retrieve_context
from backend.app.services.ai_service import generate_answer


question = "What backend experience does Abhinav have?"

context = retrieve_context(question, top_k=4)

answer = generate_answer(
    question=question,
    context=context,
)

print("\nAnswer:\n")
print(answer)