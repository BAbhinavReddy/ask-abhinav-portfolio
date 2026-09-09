from backend.app.services.rag_service import retrieve_context


query = "What backend experience does Abhinav have?"

contexts = retrieve_context(query, top_k=4)

print("\nRetrieved Context:\n")

for number, context in enumerate(contexts, start=1):
    print(f"Context {number}:")
    print(context)
    print("-" * 60)