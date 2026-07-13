from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

fake_db = []

class User(BaseModel):
    name: str
    email: str

def send_welcome_email(email: str):
    print(f"Welcome email sent to {email}")

@router.get("/")
def get_users():
    return fake_db

@router.post("/", status_code=201)
def create_user(user: User, background_tasks: BackgroundTasks):

    for existing_user in fake_db:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )

    fake_db.append(user.model_dump())

    background_tasks.add_task(send_welcome_email, user.email)

    return user

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends

security = HTTPBearer(auto_error=False)

@router.get("/me")
def get_me(credentials: HTTPAuthorizationCredentials = Depends(security)):

    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )

    return {"message": "Welcome"}