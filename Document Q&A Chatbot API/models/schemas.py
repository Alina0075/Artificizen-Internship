from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id:str
    query:str
    
class Source(BaseModel):
    filename:str
    chunk_index:int

class ChatResponse(BaseModel):
    answer:str
    sources:list[Source]