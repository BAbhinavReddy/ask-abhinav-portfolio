from backend.app.services.embedding_service import embeddings
from backend.app.services.pinecone_service import index


query = "What backend technologies does Abhinav use?"

query_vector = embeddings.embed_query(query)

results = index.query(
    vector=query_vector,
    top_k=4,
    include_metadata=True,
    namespace="portfolio",
)

print("\nTop matches:\n")

for match in results.matches:
    print(f"Score: {match.score}")
    print(f"Source: {match.metadata['source']}")
    print(f"Chunk: {match.metadata['chunk_number']}")
    print(f"Text: {match.metadata['text']}")
    print("-" * 60)