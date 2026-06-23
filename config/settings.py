import os
from dotenv import load_dotenv

load_dotenv("config/.env")

PROJECT_NAME = os.getenv("PROJECT_NAME")

MODEL_NAME = os.getenv("MODEL_NAME")

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")

PDF_FOLDER = os.getenv("PDF_FOLDER")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")