import streamlit as st
import os
from retrieval import initialize_chain

UPLOAD_FOLDER = "uploaded_files"

def save_uploaded_file(uploaded_file):
    """Save the uploaded file locally."""
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path

def main():
    st.title("📄 RAG Chatbot with gemma3:1b")

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Sidebar for file upload
    with st.sidebar:
        st.header("Upload a PDF")
        uploaded_file = st.file_uploader("Choose a file", type=["pdf"])

    if uploaded_file:
        with st.spinner("Processing document..."):
            file_path = save_uploaded_file(uploaded_file)
            qa_chain = initialize_chain(pdf_path=file_path)
        st.sidebar.success(f"✅ '{uploaded_file.name}' uploaded successfully!")

        # Display chat history
        st.subheader("Chat History")
        for chat in st.session_state.chat_history:
            st.write(f"**You:** {chat['question']}")
            st.write(f"**🤖 Chatbot:** {chat['answer']}")
            st.divider()

        # User input field
        user_query = st.text_input("Ask a question:")
        if user_query:
            with st.spinner("Generating response..."):
                response = qa_chain.run(user_query)

            # Store in chat history
            st.session_state.chat_history.append({"question": user_query, "answer": response})

            # Display latest response
            st.write("**🤖 Chatbot:**", response)

if __name__ == "__main__":
    main()

