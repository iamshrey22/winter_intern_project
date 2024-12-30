# main.py
from loader import load_and_split_document
from embeddings import get_embeddings_model
from vectorstore import initialize_vectorstore
from constants import PDF_PATH, QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME

if __name__ == "__main__":
    # Load and split the document
    print("Loading and splitting document...")
    docs = load_and_split_document(PDF_PATH)

    # Initialize embeddings model
    print("Initializing embeddings model...")
    embeddings = get_embeddings_model()

    # Set up vector store
    print("Setting up vector store...")
    vectorstore = initialize_vectorstore(
        docs, embeddings, QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME
    )

    print(f"Successfully indexed {len(docs)} document chunks into Qdrant.")
