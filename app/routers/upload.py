import os
import shutil
import uuid
from qdrant_client.models import PointStruct
from fastapi import APIRouter,UploadFile,File, Depends, HTTPException
from app.services.qdrant_db import client, collection_name
from sqlalchemy.orm import Session
from app.services.chunker import chunk_text
from app.database.database import get_db
from app.database.models import FileStatus, UploadedFile, ChatRoom
from app.services.embedder import get_embedding
from app.schemas.upload import UploadResponse
from app.services.auth import get_current_user
from app.services.ingestion.csv_file import extract_csv
from app.services.ingestion.docx import extract_docx
from app.services.ingestion.pdf import extract_pdf
from app.services.ingestion.txt import extract_txt
from app.services.ingestion.markdown import extract_md
from app.services.ingestion.pptx import extract_pptx
from app.services.ingestion.image import extract_image
from app.services.ingestion.audio import extract_audio
from app.services.ingestion.video import extract_video

router=APIRouter(prefix="/upload",tags=["Upload"])
upload_folder="uploads"

os.makedirs(upload_folder, exist_ok=True)
@router.post("/{room_id}",response_model=UploadResponse)
def upload_file(room_id:int,file:UploadFile=File(...),db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    room=(db.query(ChatRoom).filter(ChatRoom.id==room_id,ChatRoom.owner_id==current_user.id).first())
    if room is None:
        raise HTTPException(status_code=404,detail="Chat room not found")
    
    save_path=os.path.join(upload_folder,file.filename)
    
    with open(save_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    try:    
        uploaded=UploadedFile(
            room_id=room_id,
            filename=file.filename,
            file_type=file.filename.split(".")[-1].lower(),
            file_path=save_path,
            status=FileStatus.PROCESSING,
        )
        
        extension=uploaded.filename.split(".")[-1].lower()
        if extension=="csv":
            texts=extract_csv(save_path)
        elif extension=="docx":
            texts=extract_docx(save_path)
        elif extension=="pdf":
            texts=extract_pdf(save_path)
        elif extension=="txt":
            texts=extract_txt(save_path)
        elif extension=="md":
            texts=extract_md(save_path)
        elif extension=="pptx":
            texts=extract_pptx(save_path)
        elif extension in ["jpg","jpeg","png"]:
            texts=extract_image(save_path)
        elif extension in ["mp3","wav","flac"]:
            texts=extract_audio(save_path)
        elif extension in ["mp4","avi","mov"]:
            texts=extract_video(save_path)
        else:
            raise HTTPException(status_code=400,detail="Unsupported file type")
        
        db.add(uploaded)
        db.commit()
        db.refresh(uploaded)
        
        chunks=[]
        for text in texts:
            chunks.extend(chunk_text(text))
        
        vectors=[]
        for chunk in chunks:
            vectors.append(get_embedding(chunk))
        
        for i, (chunk,vector) in enumerate(zip(chunks,vectors)):
            client.upsert(
                collection_name=collection_name,
                points=[
                    PointStruct(
                        id=uuid.uuid4(),
                        vector=vector,
                        payload={
                            "room_id":room_id,
                            "file_id":uploaded.id,
                            "filename":uploaded.filename,
                            "chunk_index":i,
                            "file_type":extension,
                            "text":chunk
                        }
                        
                    )
                    
                ]
                
            )
        print("All chunks stored successfully")
        
        print("Extracted documents:", len(texts))
        print("Chunks created:", len(chunks))
        print("Embeddings created:", len(vectors))
    
        db.commit()
        db.refresh(uploaded)
        
    except Exception as e:
        db.rollback()
        uploaded.status = FileStatus.FAILED
        uploaded.error_message = str(e)
        
        db.add(uploaded)
        db.commit()
        
        raise HTTPException(status_code=500, detail=str(e))
    
    return UploadResponse(
        file_id=uploaded.id,
        filename=uploaded.filename,
        status=FileStatus.UPLOADED,
        message="File uploaded successfully"
    )
