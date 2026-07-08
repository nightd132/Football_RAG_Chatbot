from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from config import CHUNK_OVERLAP, CHUNK_SIZE
from models import load_embedding_model

jina = "http://r.jina.ai/"
source_urls = ["https://en.wikipedia.org/wiki/FIFA_World_Cup", "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026", "https://www.bbc.com/sport/football/world-cup"]

urls = []

for url in source_urls:
    urls.append(jina + url)

splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

loader = WebBaseLoader(web_paths=urls)
docs = loader.load()
chunks = splitter.split_documents(docs)

embedding = load_embedding_model()

vectorstore = Chroma.from_documents(chunks, embedding, persist_directory="chroma_db")