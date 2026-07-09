from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from config import OLLAMA_EMBEDDING_MODEL, VECTOR_STORE_DIR, TOP_K, SIMILAR_SCORE_THRESHOLD

def load_vector_space():
    vectorstore = Chroma(persist_directory=VECTOR_STORE_DIR, embedding_function=OllamaEmbeddings(model=OLLAMA_EMBEDDING_MODEL))
    return vectorstore

def search_vector_space(vectorstore, query, k=TOP_K, score_threshold=SIMILAR_SCORE_THRESHOLD):
    results = vectorstore.similarity_search_with_score(query, k=k)
    documents = []
    for document, score in results:
        print(score)
        if score <= score_threshold:
            documents.append(document)
    return documents