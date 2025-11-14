# test_vector_store.py
"""
Test script for PDF loading and vector store creation.

This script:
1. Loads and splits PDFs from the data/raw/ directory.
2. Creates a vector store from the chunks.
3. Runs a similarity search query and prints results.
"""
from document_loader import load_and_split_pdfs
from vector_store import create_vector_store


def main():
    # Step 1: Load and split PDFs
    #print("🔹 Loading and splitting PDFs...")
    #chunks = load_and_split_pdfs("data/raw/")
    #print(f"✅ Loaded {len(chunks)} chunks.")

    # Step 2: Create vector store
    #print("🔹 Creating vector store...")
    #vector_store = create_vector_store(chunks)
    #print("✅ Vector store created.")

    # Step 3: Test similarity search
    query = "What is ASIL level?"
    print(f"\n🔍 Running similarity search for query: '{query}'")
    results = vector_store.similarity_search(query, k=3)

    # Display the top result
    if results:
        print("\n🧠 Top result:\n")
        print(results[0].page_content)
    else:
        print("⚠️ No results found.")



if __name__ == "__main__":
    main()
