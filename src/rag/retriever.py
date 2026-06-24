from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="./chromadb",
    embedding_function=embedding_model
)

retriever = vector_db.as_retriever(
    search_kwargs={
        "k": 5
    }
)

print("Retriever Created Successfully")