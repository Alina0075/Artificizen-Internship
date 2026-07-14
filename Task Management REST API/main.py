from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request

from database import Base, engine
from routers import auth, tasks

Base.metadata.create_all(bind=engine)
app=FastAPI(title="Task Management API")

origins=[ "http://localhost:3000",
    "http://127.0.0.1:3000"]
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"],)

app.exception_handler(Exception)
async def global_exception_handler(request:Request, exc: Exception):
    return JSONResponse(status_code=500, content={"success":False, "message":str(exc)})

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():

    return {
        "message": "Task Management API Running"
    }