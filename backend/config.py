import os
from dotenv import load_dotenv

load_dotenv()

if os.getenv("GOOGLE_API_KEY"):
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if os.getenv("USER_AGENT"):
    USER_AGENT = os.getenv("USER_AGENT")

OLLAMA_EMBEDDING_MODEL = "nomic-embed-text"
OLLAMA_CHAT_MODEL = "qwen2.5:3B"
VECTOR_STORE_DIR = "chroma_db"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 0
TOP_K = 2

TEMPERATURE = 0.7