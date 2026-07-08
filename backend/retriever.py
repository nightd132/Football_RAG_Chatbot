from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from config import OLLAMA_EMBEDDING_MODEL, VECTOR_STORE_DIR, TOP_K

def load_vector_space():
    vectorstore = Chroma(persist_directory=VECTOR_STORE_DIR, embedding_function=OllamaEmbeddings(model=OLLAMA_EMBEDDING_MODEL))
    return vectorstore

def search_vector_space(vectorstore, query, k=TOP_K):
    results = vectorstore.similarity_search(query, k=k)
    return results