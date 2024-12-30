# vectorstore.py
from langchain_community.vectorstores import Qdrant

def initialize_vectorstore(docs, embeddings, qdrant_url, qdrant_api_key, collection_name, force_recreate=True):
    """Set up and return a Qdrant vector store."""
    return Qdrant.from_documents(
        docs,
        embeddings,
        url=qdrant_url,
        prefer_grpc=True,
        api_key=qdrant_api_key,
        collection_name=collection_name,
        force_recreate=force_recreate,
    )
