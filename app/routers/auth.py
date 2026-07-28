from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.database.database import get_db
from app.database.models import User

from app.schemas.auth import (
    UserRegister,
    UserLogin,
    Token
)

from app.services.auth import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register", status_code=201)
def register(user:UserRegister,db:Session=Depends(get_db)):
    existing=(db.query(User).filter((User.email==user.email)).first())
    if existing:
        raise HTTPException(
            400,
            detail="Email already registered"
        )
    existing_username = db.query(User).filter(User.username == user.username).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already taken"
        )
    new_user=User(username=user.username,email=user.email,hashed_password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"User registered successfully"}


    
@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(User)
        .filter(User.email == form_data.username)
        .first()
    )

    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(form_data.password, existing_user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token({"sub": existing_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }