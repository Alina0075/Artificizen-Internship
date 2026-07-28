from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import ChatRoom, User
from app.schemas.room import RoomCreate, RoomResponse
from app.services.auth import get_current_user

router = APIRouter(
    prefix="/rooms",
    tags=["Chat Rooms"]
)

@router.post("/", response_model=RoomResponse)
def create_room(room: RoomCreate, db: Session=Depends(get_db), current_user: User = Depends(get_current_user)):
    existing=(db.query(ChatRoom).filter(ChatRoom.owner_id==current_user.id, ChatRoom.name==room.name).first())
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Room with this name already exists for the user"
        )
    new_room=ChatRoom(name=room.name, description=room.description, owner_id=current_user.id)
    
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

@router.get("/", response_model=list[RoomResponse])
def get_rooms(db:Session=Depends(get_db), current_user: User = Depends(get_current_user)):
    rooms=db.query(ChatRoom).filter(ChatRoom.owner_id==current_user.id).all()
    return rooms

@router.delete("/{room_id}")
def delete_room(room_id:int, db:Session=Depends(get_db), current_user: User = Depends(get_current_user)):
    room=db.query(ChatRoom).filter(ChatRoom.id==room_id, ChatRoom.owner_id==current_user.id).first()
    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found."
        )
    db.delete(room)
    db.commit()
    return {"message":"Room deleted successfully"}
    