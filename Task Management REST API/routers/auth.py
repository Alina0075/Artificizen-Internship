from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from database import get_db
from models import User
from schema import UserCreate, UserResponse, Tokens
from utils import hash, verify
from oauth2 import create_access_token

router=APIRouter(prefix='/auth', tags=["Authentication"])
@router.post("/register",response_model=UserResponse)
def register(user:UserCreate, db:Session=Depends(get_db)):
    existing=db.query(User).filter(User.username==user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user=User(username=user.username,password=hash(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login",response_model=Tokens)
def login(user_credentials: OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    user=db.query(User).filter(User.username==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credientials")
    if not verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token=create_access_token({"user_id":user.id})
    return {
        "access_token": token,
        "token_type": "bearer"
    }
    
    