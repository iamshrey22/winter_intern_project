# embeddings.py
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings_model(model_name="sentence-transformers/all-mpnet-base-v2"):
    """Initialize and return the embeddings model."""
    return HuggingFaceEmbeddings(model_name=model_name)
