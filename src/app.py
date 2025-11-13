import streamlit as st
from src.rag_chain import query_rag
import time

# Page configuration
st.set_page_config(
    page_title="ISO 26262 Safety Assistant",
    page_icon="🚗",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stTextInput > div > div > input {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("🚗 ISO 26262 Functional Safety Assistant")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This AI assistant helps you understand **ISO 26262** Functional Safety standards.

    **Features:**
    - Ask questions about ASIL levels
    - Understand safety concepts
    - Get answers with source citations

    **Powered by:**
    - 🤖 Groq LLaMA 3.1
    - 📚 12 ISO 26262 PDFs (808 pages)
    - 🔍 RAG (Retrieval-Augmented Generation)
    """)

    st.markdown("---")
    st.markdown("**Example Questions:**")
    st.markdown("""
    - What is ASIL D?
    - Explain the V-model
    - What is a safety goal?
    - Define FTTI
    """)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sources" in message:
            with st.expander("📚 View Sources"):
                for i, source in enumerate(message["sources"], 1):
                    st.markdown(f"**{i}.** {source}")

# Chat input
if prompt := st.chat_input("Ask a question about ISO 26262..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("🔍 Searching ISO 26262 documents..."):
            try:
                response = query_rag(prompt)
                answer = response["answer"]
                sources = response["sources"]

                # Display answer
                st.markdown(answer)

                # Format sources
                source_list = []
                for doc in sources[:3]:  # Show top 3 sources
                    source_file = doc.metadata.get('source', 'unknown').split('\\')[-1]
                    source_page = doc.metadata.get('page', '?')
                    source_list.append(f"{source_file} (page {source_page})")

                # Display sources in expander
                with st.expander("📚 View Sources"):
                    for i, source in enumerate(source_list, 1):
                        st.markdown(f"**{i}.** {source}")

                # Add to chat history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": source_list
                })

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Make sure the vector store is created. Run `python test_vector_store.py` first.")

# Clear chat button in sidebar
with st.sidebar:
    st.markdown("---")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with ❤️ using LangChain, Groq, and Streamlit</p>",
    unsafe_allow_html=True
)