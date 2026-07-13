from fastapi import FastAPI
from routers import users, auth

app=FastAPI()
app.include_router(users.router)
app.include_router(auth.router)

from fastapi import Request
@app.middleware('http')
async def log_request(request: Request,call_next):
    response=await call_next(request)
    print(
        request.method,
        request.url.path,
        response.status_code
    )
    return response

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(CORSMiddleware,allow_origins=[
        "http://localhost:3000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import Request
@app.exception_handler(HTTPException)

async def http_exception_handler(
    request: Request,
    exc: HTTPException
):

    return JSONResponse(
        status_code=exc.status_code,
        content={"error": True,"detail": exc.detail,"status": exc.status_code}
    )
    
@app.get("/test-error")
def test_error():
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )