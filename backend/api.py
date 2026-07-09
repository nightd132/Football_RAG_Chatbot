from fastapi import FastAPI
from pydantic import BaseModel
from generation import generate_answer
from models import load_chat_model, load_embedding_model
from retriever import load_vector_space, search_vector_space


app = FastAPI()

llm = load_chat_model()
vectorstore = load_vector_space()

class ChatRequest(BaseModel):
    query: str

@app.post("/chat")
async def chat(request: ChatRequest):
    query = request.query
    documents = search_vector_space(vectorstore, query)
    answer = generate_answer(llm, query, documents)
    sources = {document.metadata["source"] for document in documents}
    return {"answer": answer, "sources": sources}

@app.get("/health")
def health_check():
    return {"status": "OK"}