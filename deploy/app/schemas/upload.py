from pydantic import BaseModel

class UploadResponse(BaseModel):
    file_id:int
    filename:str
    status:str
    message:str
    
