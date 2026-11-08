from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
import os

def create_db():
    embedding = HuggingFaceEmbeddings()

    docs_path = "RAG/docs"
    documents = []

    for file in os.listdir(docs_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(docs_path, file))
            documents.extend(loader.load())

    db = Chroma.from_documents(documents, embedding, persist_directory="db")

    return db