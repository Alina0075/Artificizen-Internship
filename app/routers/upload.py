import os
import shutil
import uuid

from qdrant_client.models import (
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue
)

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.qdrant_db import client, collection_name
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


router = APIRouter(prefix="/upload", tags=["Upload"])

upload_folder = "uploads"

os.makedirs(upload_folder, exist_ok=True)


@router.post("/{room_id}", response_model=UploadResponse)
def upload_file(
    room_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    room = (
        db.query(ChatRoom)
        .filter(
            ChatRoom.id == room_id,
            ChatRoom.owner_id == current_user.id
        )
        .first()
    )

    if room is None:
        raise HTTPException(
            status_code=404,
            detail="Chat room not found"
        )

    extension = file.filename.split(".")[-1].lower()

    allowed_extensions = [
        "csv",
        "docx",
        "pdf",
        "txt",
        "md",
        "pptx",
        "jpg",
        "jpeg",
        "png",
        "mp3",
        "wav",
        "flac",
        "mp4",
        "avi",
        "mov"
    ]

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )

    old_files = (
        db.query(UploadedFile)
        .filter(
            UploadedFile.room_id == room_id,
            UploadedFile.filename == file.filename
        )
        .all()
    )

    unique_filename = (
        f"{uuid.uuid4()}_{file.filename}"
    )

    save_path = os.path.join(
        upload_folder,
        unique_filename
    )
    try:

        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        uploaded = UploadedFile(
            room_id=room_id,
            filename=file.filename,
            file_type=extension,
            file_path=save_path,
            status=FileStatus.PROCESSING
        )

        db.add(uploaded)
        db.commit()
        db.refresh(uploaded)

        if extension == "csv":
            texts = extract_csv(save_path)

        elif extension == "docx":
            texts = extract_docx(save_path)

        elif extension == "pdf":
            texts = extract_pdf(save_path)

        elif extension == "txt":
            texts = extract_txt(save_path)

        elif extension == "md":
            texts = extract_md(save_path)

        elif extension == "pptx":
            texts = extract_pptx(save_path)

        elif extension in ["jpg", "jpeg", "png"]:
            texts = extract_image(save_path)

        elif extension in ["mp3", "wav", "flac"]:
            texts = extract_audio(save_path)

        elif extension in ["mp4", "avi", "mov"]:
            texts = extract_video(save_path)

        chunks = []

        for text in texts:
            chunks.extend(
                chunk_text(text)
            )

        print(
            "Extracted documents:",
            len(texts)
        )

        print(
            "Chunks created:",
            len(chunks)
        )

        vectors = []

        for chunk in chunks:
            vectors.append(
                get_embedding(chunk)
            )

        print(
            "Embeddings created:",
            len(vectors)
        )

        for i, (chunk, vector) in enumerate(
            zip(chunks, vectors)
        ):

            client.upsert(
                collection_name=collection_name,
                points=[
                    PointStruct(
                        id=uuid.uuid4(),
                        vector=vector,
                        payload={
                            "room_id": room_id,
                            "file_id": uploaded.id,
                            "filename": uploaded.filename,
                            "chunk_index": i,
                            "file_type": extension,
                            "text": chunk
                        }
                    )
                ]
            )

        print(
            "New file chunks stored successfully"
        )


        for old_file in old_files:

            client.delete(
                collection_name=collection_name,
                points_selector=Filter(
                    must=[
                        FieldCondition(
                            key="file_id",
                            match=MatchValue(
                                value=old_file.id
                            )
                        )
                    ]
                )
            )

            if (
                old_file.file_path
                and os.path.exists(old_file.file_path)
            ):
                os.remove(
                    old_file.file_path
                )

            db.delete(old_file)

        uploaded.status = FileStatus.UPLOADED

        db.commit()
        db.refresh(uploaded)

        return UploadResponse(
            file_id=uploaded.id,
            filename=uploaded.filename,
            status=FileStatus.UPLOADED,
            message="File uploaded successfully"
        )

    except Exception as e:

        print(
            "UPLOAD ERROR:",
            str(e)
        )


        try:
            uploaded.status = FileStatus.FAILED
            uploaded.error_message = str(e)

            db.commit()
            db.refresh(uploaded)

        except Exception as db_error:

            print(
                "FAILED TO UPDATE UPLOAD STATUS:",
                str(db_error)
            )

            db.rollback()

        if os.path.exists(save_path):

            try:
                os.remove(save_path)

            except Exception as file_error:

                print(
                    "FAILED TO REMOVE UPLOAD:",
                    str(file_error)
                )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.get("/{room_id}/files")
def get_files(
    room_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    room = (
        db.query(ChatRoom)
        .filter(
            ChatRoom.id == room_id,
            ChatRoom.owner_id == current_user.id
        )
        .first()
    )

    if room is None:
        raise HTTPException(
            status_code=404,
            detail="Chat room not found"
        )

    files = (
        db.query(UploadedFile)
        .filter(UploadedFile.room_id == room_id)
        .order_by(UploadedFile.id.desc())
        .all()
    )

    return [
        {
            "id": file.id,
            "filename": file.filename,
            "file_type": file.file_type,
            "status": file.status.value
                if hasattr(file.status, "value")
                else file.status,
            "error_message": file.error_message
        }
        for file in files
    ]

@router.delete("/{room_id}/{file_id}")
def delete_file(
    room_id: int,
    file_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    room = (
        db.query(ChatRoom)
        .filter(
            ChatRoom.id == room_id,
            ChatRoom.owner_id == current_user.id
        )
        .first()
    )

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )

    file = (
        db.query(UploadedFile)
        .filter(
            UploadedFile.id == file_id,
            UploadedFile.room_id == room_id
        )
        .first()
    )

    if not file:
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    try:
        client.delete(
            collection_name=collection_name,
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="file_id",
                        match=MatchValue(
                            value=file.id
                        )
                    )
                ]
            )
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to delete file from vector database: {str(e)}"
        )

    if file.file_path and os.path.exists(file.file_path):
        try:
            os.remove(file.file_path)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to delete physical file: {str(e)}"
            )

    # Delete database record
    db.delete(file)
    db.commit()

    return {
        "message": "File deleted successfully",
        "file_id": file_id
    }