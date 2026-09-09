from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.app.services.embedding_service import embeddings
from backend.app.services.pinecone_service import index


KNOWLEDGE_DIR = Path(__file__).resolve().parents[3] / "knowledge"


def load_knowledge_files():
    documents = []

    for file_path in KNOWLEDGE_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append(
            {
                "text": text,
                "source": file_path.name,
            }
        )

    return documents


def create_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100,
    )

    chunks = []

    for document in documents:
        split_texts = splitter.split_text(
            document["text"]
        )

        for chunk_number, text in enumerate(split_texts):
            chunks.append(
                {
                    "text": text,
                    "source": document["source"],
                    "chunk_number": chunk_number,
                }
            )

    return chunks


def ingest():
    documents = load_knowledge_files()

    print(f"Loaded {len(documents)} knowledge files.")

    chunks = create_chunks(documents)

    print(f"Created {len(chunks)} chunks.")

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    vectors = embeddings.embed_documents(texts)

    print(f"Generated {len(vectors)} embeddings.")
    print(f"Embedding dimension: {len(vectors[0])}")

    pinecone_vectors = []

    for chunk, vector in zip(chunks, vectors):
        pinecone_vectors.append(
            {
                "id": f"{chunk['source']}-{chunk['chunk_number']}",
                "values": vector,
                "metadata": {
                    "source": chunk["source"],
                    "chunk_number": chunk["chunk_number"],
                    "text": chunk["text"],
                },
            }
        )

    index.upsert(
        vectors=pinecone_vectors,
        namespace="portfolio",
    )

    print(f"Uploaded {len(pinecone_vectors)} vectors to Pinecone.")



if __name__ == "__main__":
    ingest()