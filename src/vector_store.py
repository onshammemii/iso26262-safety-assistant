from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def create_vector_store(chunks, persist_directory: str = "data/vector_store"):
    """
    Create FAISS vector store from document chunks
    """
    # Use free embeddings model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create vector store
    vector_store = FAISS.from_documents(chunks, embeddings)

    # Save locally
    vector_store.save_local(persist_directory)
    print(f"Vector store saved to {persist_directory}")

    return vector_store


def load_vector_store(persist_directory: str = "data/vector_store"):
    """
    Load existing vector store
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vector_store = FAISS.load_local(
        persist_directory,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vector_store