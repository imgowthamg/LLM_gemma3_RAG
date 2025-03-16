import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import CHUNK_SIZE, CHUNK_OVERLAP, MODEL_NAME

def load_and_process_pdf(pdf_path):
    """Loads, splits PDF into chunks, and returns processed docs."""
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    st.write(f"Loaded {len(documents)} document(s).")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )
    docs = text_splitter.split_documents(documents)
    st.write(f"Split into {len(docs)} chunks.")

    return docs

def generate_embeddings():
    """Loads HuggingFace embeddings model."""
    return HuggingFaceEmbeddings(model_name=MODEL_NAME)

