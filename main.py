# main.py
from loader import load_and_split_document
from embeddings import get_embeddings_model
from vectorstore import initialize_vectorstore
from constants import PDF_PATH, QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME


#uncomment for user input
# import os
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename

# def select_pdf_file():
#     """Open a file dialog to select a PDF file."""
#     Tk().withdraw()  # Hide the root tkinter window
#     file_path = askopenfilename(
#         title="Select a PDF file",
#         filetypes=[("PDF files", "*.pdf")]
#     )
#     if not file_path:
#         raise ValueError("No file selected.")
#     return file_path

    




if __name__ == "__main__":

    #uncomment for user input
    # print("Please select a PDF file.")
    # PDF_PATH = select_pdf_file()

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
