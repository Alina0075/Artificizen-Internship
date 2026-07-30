from fastapi import FastAPI
from app.database.database import Base
from app.database.database import engine
from app.routers import auth
from app.routers import rooms
from app.routers import upload
from app.routers import chat

app = FastAPI(
    title="CyberRAG API",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(rooms.router)
app.include_router(upload.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "Welcome to the CyberRAG API!"}
