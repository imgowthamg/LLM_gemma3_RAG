# RAG Chatbot with LangChain and Ollama's Gemma3 Models

This project implements a Retrieval-Augmented Generation (RAG) chatbot that processes PDF documents and answers user queries based on their content. It leverages LangChain for document processing and retrieval, FAISS for vector storage, and Ollama's Gemma3 models for language understanding and response generation. The user interface is built using Streamlit.

## Features

- **PDF Upload:** Users can upload PDF files to serve as the knowledge base for the chatbot.
- **Efficient Retrieval:** Utilizes FAISS for fast and efficient document retrieval.
- **Language Models:** Supports various sizes of Gemma3 models (1B, 4B, 12B, 27B parameters) to cater to different resource capabilities.
- **Interactive UI:** Provides a user-friendly interface using Streamlit for seamless interaction.

## Installation

### Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed on your local machine

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/imgowthamg/LLM_gemma3_RAG.git
   cd LLM_gemma3_RAG
2. Python venv step
   '''bash
  python3 -m venv venv  # Create virtual environment
  source venv/bin/activate  # Activate it (Windows: venv\Scripts\activate)
  pip install -r requirements.txt  # Magic dependencies installer
