from backend.app.services.embedding_service import embeddings


text = "Abhinav builds Python backend APIs using FastAPI."

vector = embeddings.embed_query(text)

print(f"Vector dimension: {len(vector)}")
print(f"First five values: {vector[:5]}")