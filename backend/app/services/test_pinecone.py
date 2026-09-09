from backend.app.services.pinecone_service import index


stats = index.describe_index_stats()

print(stats)