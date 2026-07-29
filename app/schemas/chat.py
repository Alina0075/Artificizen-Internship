from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    query:str

class Source(BaseModel):
    filename:str
    chunk_index:str

class ChatResponse(BaseModel):
    answer:str
    sources:List[Source]
    
