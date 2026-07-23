import os

from fastapi import APIRouter, UploadFile, File, HTTPException

from services.file_reader import extract_text
from services.chunking import chunk_text
from services.embeddings import get_embeddings
from services.qdrant_service import store_chunks

router = APIRouter(
    tags=["Document Ingestion"]
)

upload_folder="uploads"
os.makedirs(upload_folder,exist_ok=True)

@router.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    if not file.filename.endswith(('.txt','.pdf')):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Only .txt and .pdf files are supported."
        )
    file_path=os.path.join(upload_folder,file.filename)
    
    #saving the uploaded file
    with open(file_path,'wb') as f:
        f.write(await file.read())
        
    text=extract_text(file_path)
    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="The uploaded document is empty."
        )
    chunks=chunk_text(text)
    embeddings=[get_embeddings(chunk) for chunk in chunks]
    store_chunks(chunks=chunks, embeddings=embeddings, filename=file.filename)
    
    return{
        "messages": "Document indexed successfully.",
        "filename": file.filename,
        "chunks": len(chunks)
    }