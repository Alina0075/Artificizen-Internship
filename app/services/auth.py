import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import User

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
auth_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data:dict, expires_delta:timedelta=None):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token:str=Depends(auth_scheme), db:Session=Depends(get_db)):
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Token",
        headers={"WWW-Authenticate":"Bearer"},
    )
    
    try:
        playload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        emial=playload.get("sub")
        if emial is None:
            raise credentials_exception
    
    except JWTError:
        raise credentials_exception
    
    user=(db.query(User).filter(User.email==emial).first())
    
    if user is None:
        raise credentials_exception
    return user