from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import PromptTemplate

from src.vector_store import load_vector_store
from dotenv import load_dotenv

load_dotenv()


from langchain_groq import ChatGroq
import os



def create_rag_chain():
    """
    Create RAG chain with Groq (free API)
    """
    print("Loading vector store...")
    vector_store = load_vector_store()

    print("Initializing Groq LLM...")
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3
    )

    prompt_template = """You are an expert in ISO 26262 Functional Safety standards.
    Use the context to answer the question.
    If you don't know, say "I don't have enough information."

    Context: {context}

    Question: {question}

    Answer:"""

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    print("Creating RAG chain...")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 4}),
        chain_type_kwargs={"prompt": PROMPT},
        return_source_documents=True
    )

    return qa_chain


def query_rag(question: str):
    chain = create_rag_chain()
    result = chain.invoke({"query": question})

    return {
        "answer": result["result"],
        "sources": result["source_documents"]
    }