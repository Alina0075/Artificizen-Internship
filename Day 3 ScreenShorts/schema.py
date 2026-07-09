from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True


class PostResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True