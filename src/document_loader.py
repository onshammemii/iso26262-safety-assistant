from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os


def load_and_split_pdfs(pdf_directory: str, chunk_size: int = 1000):
    """
    Load PDFs and split into chunks
    """
    documents = []

    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, filename)
            print(f"Loading: {filename}")
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()
            documents.extend(docs)
            print(f"  -> Loaded {len(docs)} pages")

    print(f"\nTotal pages loaded: {len(documents)}")

    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=200,  # Overlap to maintain context
        separators=["\n\n", "\n", ".", " "]
    )

    chunks = text_splitter.split_documents(documents)
    print(f"Total chunks created: {len(chunks)}")

    return chunks