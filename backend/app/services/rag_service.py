from backend.app.services.embedding_service import embeddings
from backend.app.services.pinecone_service import index


def retrieve_context(query: str, top_k: int = 4) -> list[str]:
    query_vector = embeddings.embed_query(query)

    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True,
        namespace="portfolio",
    )

    contexts = []

    for match in results.matches:
        metadata = match.metadata

        if metadata and "text" in metadata:
            contexts.append(metadata["text"])

    return contexts