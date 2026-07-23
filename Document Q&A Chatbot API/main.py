from fastapi import FastAPI
from routers.ingest import router as ingest_router
from routers.chat import router as chat_router
app=FastAPI(title="Document Q&A Chatbot", description="RAG-powered chatbot using FastAPI, Groq, Sentence Transformers, and Qdrant",
    version="1.0.0")

app.include_router(ingest_router)
app.include_router(chat_router)
@app.get("/")
def get_home():
    return {"message": "Welcome to the Document Q&A Chatbot API!"}