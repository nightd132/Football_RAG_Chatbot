from langchain_ollama import ChatOllama, OllamaEmbeddings
# from langchain_google_genai import ChatGoogleGenerativeAI
from config import OLLAMA_EMBEDDING_MODEL, OLLAMA_CHAT_MODEL, TEMPERATURE

def load_chat_model(temperature=TEMPERATURE):
    # model = ChatGoogleGenerativeAI(model="gemini-flash-3.5")
    model = ChatOllama(model=OLLAMA_CHAT_MODEL, temperature=temperature)
    return model

def load_embedding_model():
    # embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
    embedding_model = OllamaEmbeddings(model=OLLAMA_EMBEDDING_MODEL)
    return embedding_model