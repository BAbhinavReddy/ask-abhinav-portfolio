from langchain_google_genai import ChatGoogleGenerativeAI

from backend.app.config import GOOGLE_API_KEY


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0,
)


def generate_answer(question: str, context: list[str]) -> str:
    context_text = "\n\n".join(context)

    prompt = f"""
You are "Ask Abhinav", an AI assistant representing
Abhinav Reddy Bobba.

Your job is to answer recruiter questions about Abhinav's
professional background.

Use ONLY the portfolio context provided below.

Rules:
- Do not invent experience.
- Do not invent technologies.
- Do not invent responsibilities.
- Do not invent achievements.
- Do not invent education details.
- Do not make assumptions about Abhinav.
- If the requested information is not supported by the
  portfolio context, say that the information is not
  available in the portfolio.
- Answer directly and professionally.
- Keep answers concise.
- Refer to Abhinav in the third person.
- Do not mention Pinecone, embeddings, retrieval,
  prompts, or internal implementation details.

Portfolio context:
{context_text}

Recruiter's question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content