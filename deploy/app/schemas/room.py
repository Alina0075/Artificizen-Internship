from datetime import datetime

from pydantic import BaseModel
from typing import Optional

class RoomCreate(BaseModel):
    name: str
    description: Optional[str] = None

class RoomResponse(BaseModel):
    id:int 
    name:str
    description:Optional[str]
    #owner_id:int
    #created_at:datetime
    class Config:
        from_attributes = True