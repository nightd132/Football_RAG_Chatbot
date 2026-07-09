from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from config import CHUNK_OVERLAP, CHUNK_SIZE, VECTOR_STORE_DIR
from models import load_embedding_model

from pathlib import Path

url_file = Path("data/urls.txt")



jina = "http://r.jina.ai/"
with url_file.open("r", encoding="utf-8") as f:
    source_urls = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith("#")
    ]

urls = []

for url in source_urls:
    urls.append(jina + url)

splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

loader = WebBaseLoader(web_paths=urls)
docs = loader.load()

for doc in docs:
    doc.metadata["source"] = doc.metadata["source"][len(jina):]

chunks = splitter.split_documents(docs)
print(docs[0].page_content)

embedding = load_embedding_model()

vectorstore = Chroma.from_documents(chunks, embedding, persist_directory=VECTOR_STORE_DIR)