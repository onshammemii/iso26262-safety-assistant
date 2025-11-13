# ISO 26262 Functional Safety Assistant

An intelligent question-answering system designed to help automotive engineers and safety professionals navigate the complex **ISO 26262 Functional Safety Standard**.  
This AI-powered assistant uses advanced natural language processing and retrieval-augmented generation (RAG) to provide accurate, contextual answers with **source citations** from the official ISO 26262 documentation.

---

## Live Application

**Try the live demo:** [https://iso26262-safety-assistant.streamlit.app/](https://iso26262-safety-assistant.streamlit.app/)

---

## Project Overview

**ISO 26262** is the international standard for functional safety in automotive systems, comprising over 800 pages across 12 parts.  
Finding specific information within this extensive documentation can be **time-consuming and challenging**.

This assistant solves that problem by allowing users to ask questions in natural language and receive precise answers extracted from relevant sections of the standard.

The system:
- Processes the entire ISO 26262 documentation set
- Breaks it into semantic chunks
- Uses vector embeddings for intelligent retrieval  
When a user asks a question, it identifies the most relevant passages and synthesizes a comprehensive answer — complete with citations to the original source.

---

## Technical Architecture

### Natural Language Processing
Uses **HuggingFace sentence transformers** to convert text into high-dimensional vector representations, capturing semantic meaning for robust understanding of user queries.

### Vector Database
**FAISS (Facebook AI Similarity Search)** stores and retrieves vector embeddings.  
Indexes **2,658 document chunks** extracted from **808 pages** of ISO 26262 documentation, enabling sub-second semantic search.

### Language Model
Powered by **Groq’s LLaMA 3.1 (8B parameters)** model — balancing accuracy and computational efficiency for detailed, fast responses.

### * Retrieval-Augmented Generation (RAG)
Combines semantic retrieval with large language model reasoning.  
For each query:
1. Retrieves relevant document chunks  
2. Provides them as context to the LLM  
This minimizes hallucinations and grounds answers in the official ISO text.

### User Interface
Built with **Streamlit**, providing a clean chat-based experience with:
- Conversation history  
- Source citations  
- Example questions and system info in the sidebar  

---

## Technology Stack

| Component | Technology | Purpose |
|------------|-------------|----------|
| **Backend** | LangChain | Query orchestration and RAG pipeline |
| **Embeddings** | Sentence-Transformers (`all-MiniLM-L6-v2`) | Text vectorization |
| **Vector Store** | FAISS | Semantic similarity search |
| **Language Model** | Groq API + LLaMA 3.1 | Answer generation |
| **Document Processing** | PyPDF + LangChain Text Splitters | PDF extraction and chunking |
| **Frontend** | Streamlit | Interactive UI |
| **Deployment** | Streamlit Cloud | Hosting and auto-deployment |

---

## Key Features

- **Comprehensive Coverage:** Includes all 12 parts of ISO 26262:2018  
- **Source Citations:** Each answer includes document and page references  
- **Contextual Understanding:** Semantic retrieval beyond keyword search  
- **Conversational Interface:** Follow-up questions and natural dialogue  
- **Real-time Responses:** Optimized retrieval and inference for quick replies  

---

## Use Cases

- **Safety Engineers:** Quickly locate requirements relevant to design work  
- **Project Managers:** Verify compliance requirements for projects  
- **Quality Assurance Teams:** Reference ISO clauses during audits  
- **Training & Education:** Learn ISO 26262 concepts interactively  
- **Technical Writers:** Align documentation with ISO terminology  

---

## Development Process

The project follows modern software engineering best practices:
- **Version control** with Git and modular architecture  
- **Clean separation** of document processing, vector storage, and UI layers  
- **Inline documentation** and type hints for clarity  
- **Environment-based configuration** for secure API key management  

Each module handles a specific concern:
- Document Loader → PDF processing  
- Vector Store → Embedding and retrieval  
- RAG Chain → Orchestration  
- Streamlit App → User interaction  

---

## Deployment and Operations

- **Automatic deployment** on Streamlit Cloud upon pushing to the main branch  
- **Secure secrets management** via Streamlit’s encrypted configuration  
- **Efficient startup:** Vector store created on first run, reused on redeploy  

---

## 🌟 Project Significance

This project demonstrates **how AI can make complex technical standards accessible** to engineers.  
It highlights end-to-end integration of:
- Document processing  
- Vector retrieval  
- LLM reasoning  
- Cloud deployment  

The assistant helps **automotive teams save time** navigating ISO 26262, while showcasing real-world application of **Retrieval-Augmented Generation (RAG)** and **vector search technologies**.

---

## Technical Learning Outcomes

Through this project, the developer gained hands-on experience in:
- Transformer-based embeddings for semantic search  
- Vector database indexing (FAISS)  
- Prompt engineering and RAG best practices  
- Document chunking and retrieval optimization  
- Cloud deployment and DevOps for ML applications  

---


