from fastapi import Depends, FastAPI

from auth import get_current_user, router
from database import Base, engine
from models import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@router.get("/users/me")
def read_users_me(
    current_user: User = Depends(get_current_user)
):
    return current_user