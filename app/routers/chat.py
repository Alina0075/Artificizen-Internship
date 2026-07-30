import os

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
)

from app.database.database import get_db

from app.database.models import (
    ChatRoom,
    User,
    ChatMessage,
    UploadedFile
)

from app.schemas.chat import ChatRequest

from app.services.auth import get_current_user

from app.services.retriever import search_documents
from app.services.rag import generate_answer

from app.services.qdrant_db import (
    client,
    collection_name
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/{room_id}")
def chat(
    room_id: int,
    chat_request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    room = db.query(ChatRoom).filter(
        ChatRoom.id == room_id,
        ChatRoom.owner_id == current_user.id
    ).first()

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )

    history = (
        db.query(ChatMessage)
        .filter(ChatMessage.room_id == room_id)
        .order_by(ChatMessage.created_at.asc())
        .limit(6)
        .all()
    )

    history.reverse()

    chunks = search_documents(
        room_id,
        chat_request.query
    )

    if not chunks:

        answer = "I don't know."
        sources = []

    else:

        answer = generate_answer(
            chat_request.query,
            chunks,
            history
        )

        if answer.strip().lower() == "i don't know.":

            sources = []

        else:

            sources = []

            for chunk in chunks:

                sources.append({
                    "filename": chunk["filename"],
                    "file_type": chunk["file_type"],
                    "chunk_index": chunk["chunk_index"],
                    "excerpt": chunk["text"][:150]
                })

    user_message = ChatMessage(
        room_id=room_id,
        role="user",
        content=chat_request.query
    )

    assistant_message = ChatMessage(
        room_id=room_id,
        role="assistant",
        content=answer
    )

    db.add(user_message)
    db.add(assistant_message)

    db.commit()

    return {
        "answer": answer,
        "sources": sources
    }
    
@router.get("/{room_id}/history")
def get_history(room_id:int,skip:int=0,limit:int=50,db:Session=Depends(get_db), current_user=Depends(get_current_user)):
    room=db.query(ChatRoom).filter(ChatRoom.id == room_id,
        ChatRoom.owner_id == current_user.id).first()
    
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    history=db.query(ChatMessage).filter(ChatMessage.room_id==room_id).order_by(ChatMessage.created_at.asc()).offset(skip).limit(limit).all()
    
    return [
        {
            "id":message.id,
            "role":message.role,
            "content":message.content,
            "created_at":message.created_at
        }
        for message in history
    ]

@router.delete("/{room_id}/history")
def delete_history(
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

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )


    db.query(ChatMessage).filter(
        ChatMessage.room_id == room_id
    ).delete(
        synchronize_session=False
    )


    files = (
        db.query(UploadedFile)
        .filter(
            UploadedFile.room_id == room_id
        )
        .all()
    )


    for file in files:

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

            print(
                f"Deleted Qdrant vectors for file "
                f"{file.filename} | FILE ID: {file.id}"
            )

        except Exception as e:

            print(
                f"Qdrant deletion failed for "
                f"{file.filename}: {e}"
            )



    for file in files:

        if (
            file.file_path
            and os.path.exists(file.file_path)
        ):

            try:

                os.remove(file.file_path)

                print(
                    f"Deleted physical file: "
                    f"{file.file_path}"
                )

            except Exception as e:

                print(
                    f"Failed to delete physical file "
                    f"{file.file_path}: {e}"
                )

    db.query(UploadedFile).filter(
        UploadedFile.room_id == room_id
    ).delete(
        synchronize_session=False
    )


    db.commit()

    return {
        "message": "Chat history and all workspace files deleted successfully.",
        "deleted_files": len(files)
    }