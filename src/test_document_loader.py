from src.document_loader import load_and_split_pdfs
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
print("Starting document processing...\n")

# Load and process PDFs
chunks = load_and_split_pdfs("C:/Users\ons\PycharmProjects\iso26262-safety-assistant\data/raw")


print(f"\n{'='*60}")
print(f"RESULTS:")
print(f"{'='*60}")
print(f"Total chunks created: {len(chunks)}")

print(f"\n{'='*60}")
print(f"SAMPLE CHUNK (first 500 characters):")
print(f"{'='*60}")
print(chunks[0].page_content[:500])

print(f"\n{'='*60}")
print(f"Chunk metadata:")
print(f"{'='*60}")
print(f"Source: {chunks[0].metadata.get('source', 'unknown')}")
print(f"Page: {chunks[0].metadata.get('page', 'unknown')}")

print(f"\n{'='*60}")
print("Checking different chunks:")
print(f"{'='*60}")
# Sample from beginning, middle, and end
for i in [0, len(chunks)//2, -1]:
    print(f"\nCHUNK {i}:")
    print(f"  Source: {chunks[i].metadata.get('source', 'unknown')}")
    print(f"  Page: {chunks[i].metadata.get('page', 'unknown')}")
    print(f"  Preview: {chunks[i].page_content[:150]}...")

print("\n✅ Document loading test completed!")