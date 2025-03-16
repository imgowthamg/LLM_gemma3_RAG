import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from processing import load_and_process_pdf, generate_embeddings
from llm import OllamaLLM
from config import RETRIEVAL_K

@st.cache_resource
def initialize_chain(pdf_path):
    """Creates FAISS vector store & initializes RetrievalQA chain."""
    docs = load_and_process_pdf(pdf_path)
    embeddings = generate_embeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    st.write("FAISS vector store built.")

    retriever = vectorstore.as_retriever(search_kwargs={"k": RETRIEVAL_K})
    ollama_llm = OllamaLLM()

    return RetrievalQA.from_chain_type(llm=ollama_llm, chain_type="stuff", retriever=retriever)
