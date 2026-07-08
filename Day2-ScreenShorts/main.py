from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import Field, field_validator
from datetime import datetime
app = FastAPI()

class AddressModel(BaseModel):
    city:  str
    country: str

class User(BaseModel):
    name: str
    email: str =Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    age: int = Field(ge=18, le=120, description="Age must be between 18 and 120")
    address: AddressModel
    @field_validator('name')
    def name_validation(cls,value):
        if any(char.isdigit() for char in value):
            raise ValueError('Name must not contain numbers')
        return value

class User_ID(BaseModel):
    name: str
    email: str
    age: int
    id: int
    address: AddressModel
    
@app.post('/users',response_model=User_ID)
def create_user(user: User):
    return {
        "id" : 1,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "address": user.address
    }
    
class ItemCreate(BaseModel):
    name: str
    price: float = Field(gt=0)
    in_stock: bool
    
class ItemRead(BaseModel):
    name: str
    price: float
    in_stock: bool
    created_at: datetime

@app.post('/items', response_model=ItemRead)
def create_item(item: ItemCreate):
    return {
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock,
        "created_at": datetime.now()
    }

    