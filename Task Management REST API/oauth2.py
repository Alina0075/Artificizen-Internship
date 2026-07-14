from jose import jwt, JWTError
from datetime import datetime, timedelta, UTC
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from dotenv import load_dotenv

import os

load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
)
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_access_token(data):
    to_encode=data.copy()
    expire = datetime.now(UTC) + timedelta(
    minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

def verify_token(token):
    return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])

def get_current_user(token: str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credentials_exception=HTTPException(status_code=401,detail="Invalid Credentials")
    try:
        payload=verify_token(token)
        user_id=payload.get("user_id")
    except JWTError:
        raise credentials_exception
    user=db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise credentials_exception
    return user