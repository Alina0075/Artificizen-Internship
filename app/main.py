from fastapi import FastAPI
from app.database.database import Base
from app.database.database import engine
from app.routers import auth
from app.routers import rooms

app = FastAPI(
    title="CyberRAG API",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(rooms.router)
@app.get("/")
def root():
    return {"message": "Welcome to the CyberRAG API!"}
