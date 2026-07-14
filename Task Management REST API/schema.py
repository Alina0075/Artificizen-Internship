from datetime import date
from pydantic import BaseModel, Field, ConfigDict, field_validator
from enum import Enum

class UserCreate(BaseModel):
    username:str= Field(min_length=3)
    password:str= Field(min_length=8)
    
class UserResponse(BaseModel):
    id:int
    username:str
    model_config = ConfigDict(from_attributes=True)
        
class Tokens(BaseModel):
    access_token:str
    token_type:str

class TaskStatus(str, Enum):
    pending = "pending"
    Pending = "Pending"

    in_progress = "in progress"
    In_Progress = "In Progress"

    done = "done"
    Done = "Done"

    due = "due"
    Due = "Due"
class TaskCreate(BaseModel):
    title:str
    description:str
    status:TaskStatus
    due_date:date
    @field_validator("status", mode="before")
    @classmethod
    def normalize_status(cls, value):
        if isinstance(value, str):
            return value.strip().lower()
        return value

class TaskCreate(BaseModel):
    title:str
    description:str
    status:TaskStatus
    due_date:date

class TaskResponse(TaskCreate):
    id: int
    owner_id: int
    model_config = ConfigDict(from_attributes=True)