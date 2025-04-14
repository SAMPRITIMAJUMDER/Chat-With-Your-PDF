# AWS/admin/admin.py

import streamlit as st
import boto3
import uuid
import os

from langchain_community.embeddings import BedrockEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

# --- Configuration ---
BUCKET_NAME = os.getenv("BUCKET_NAME")
if not BUCKET_NAME:
    st.error("❌ Environment variable BUCKET_NAME not set!")
    st.stop()

# --- AWS Clients ---
s3_client = boto3.client("s3")
bedrock_client = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v1",
    client=bedrock_client
)

# --- Utility Functions ---
def get_unique_id():
    return str(uuid.uuid4())

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load_and_split()

def split_text(pages, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(pages)

def create_vector_store(request_id, documents):
    try:
        vectorstore = FAISS.from_documents(documents, bedrock_embeddings)
        file_name = f"{request_id}.bin"
        folder_path = "/tmp"
        vectorstore.save_local(index_name=file_name, folder_path=folder_path)

        # Upload to S3
        s3_client.upload_file(
            Filename=os.path.join(folder_path, f"{file_name}.faiss"),
            Bucket=BUCKET_NAME,
            Key="my_faiss.faiss"
        )
        s3_client.upload_file(
            Filename=os.path.join(folder_path, f"{file_name}.pkl"),
            Bucket=BUCKET_NAME,
            Key="my_faiss.pkl"
        )
        return True
    except Exception as e:
        st.error(f"❌ Error while creating vector store: {e}")
        return False

# --- Main Streamlit App ---
def main():
    st.set_page_config(page_title="Admin - Chat with PDF", layout="centered")
    st.title("🛠 Admin Panel: Chat with PDF using AWS + Bedrock")

    uploaded_file = st.file_uploader("📄 Upload a PDF", type="pdf")
    if uploaded_file:
        request_id = get_unique_id()
        st.write(f"🆔 Request ID: `{request_id}`")

        # Save uploaded PDF locally
        saved_path = f"{request_id}.pdf"
        with open(saved_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        # Load and split PDF
        pages = load_pdf(saved_path)
        st.success(f"📚 Loaded {len(pages)} page(s) from the PDF")

        docs = split_text(pages)
        st.success(f"📝 Split into {len(docs)} chunks")

        st.subheader("🔍 Preview:")
        st.code(docs[0].page_content[:1000])  # show only a snippet

        # Create and upload vector store
        st.write("📦 Creating Vector Store and uploading to S3...")
        result = create_vector_store(request_id, docs)

        if result:
            st.success("✅ Successfully processed and stored in S3!")
        else:
            st.error("⚠️ Something went wrong during vector store creation.")

if __name__ == "__main__":
    main()
