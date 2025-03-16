# RAG Chatbot with LangChain and Ollama's Gemma3 Models


Implements a Retrieval-Augmented Generation (RAG) chatbot that processes PDF documents and answers user queries based on their content. It leverages **LangChain** for document processing and retrieval, **FAISS** for vector storage, and **Ollama's Gemma3 models** for language understanding and response generation. The user interface is built using **Streamlit**.

## Features![Screenshot from 2025-03-16 11-39-46](https://github.com/user-attachments/assets/953ca3fb-f28e-49cf-83bf-7605f034e2ab)


- **PDF Upload:** Users can upload PDF files to serve as the knowledge base for the chatbot.
- **Efficient Retrieval:** Utilizes **FAISS** for fast and efficient document retrieval.
- **Language Models:** Supports various sizes of **Gemma3 models** (1B, 4B, 12B, 27B parameters) to cater to different resource capabilities.
- **Interactive UI:** Provides a user-friendly interface using **Streamlit** for seamless interaction.

## Installation

### Prerequisites

- **Python 3.8 or higher**
- **[Ollama](https://ollama.ai/)** installed on your local machine

### Setup Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/imgowthamg/LLM_gemma3_RAG.git
   cd LLM_gemma3_RAG
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python3 -m venv venv  # Create virtual environment
   source venv/bin/activate  # Activate it (Windows: venv\Scripts\activate)
   pip install -r requirements.txt  # Install dependencies
   ```

3. **Run Your AI Model:**
   Open a separate terminal and start the Gemma3 model:
   ```bash
   ollama run gemma3:1b  # Start with 1B model
   ```
   **Note:** Larger models like `gemma3:4b`, `gemma3:12b`, and `gemma3:27b` are available but require more system resources.

4. **Run the Streamlit Application:**
   ```bash
   streamlit run app.py
   ```

## File Structure

```
LLM_gemma3_RAG/
├── app.py          # UI
├── config.py       # Configuration settings
├── llm.py          # AI model integration
├── processing.py   # PDF processing 
├── retrieval.py    # FAISS-based document retrieval
```

## Usage

1. Upload a PDF file via the Streamlit UI.
2. Ask questions based on the uploaded content.
3. The chatbot will retrieve relevant information and generate responses using the Gemma3 model.


## Acknowledgments

- [LangChain](https://www.langchain.com/) for seamless integration of LLMs.
- [FAISS](https://faiss.ai/) for efficient vector search.
- [Ollama](https://ollama.ai/) for hosting powerful Gemma3 models.
- [Streamlit](https://streamlit.io/) for the interactive UI.



