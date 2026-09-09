from langchain_google_genai import GoogleGenerativeAIEmbeddings

from backend.app.config import GOOGLE_API_KEY


embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY,
)