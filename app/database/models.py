from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, JSON, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
import enum 

class FileStatus(str,enum.Enum):
    PROCESSING = "PROCESSING"
    UPLOADED = "UPLOADED"
    FAILED = "FAILED"

class MessageRole(str,enum.Enum):
    USER = "user"
    ASSISTANT = "assistant"

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50),unique=True,index=True,nullable=False)
    email=Column(String(100),unique=True,index=True,nullable=False)
    hashed_password=Column(String(255),nullable=False)
    created_at=Column(DateTime(timezone=True),default=datetime.utcnow)
    rooms=relationship("ChatRoom",back_populates="owner")
    messages=relationship("ChatMessage",back_populates="user")
    
class ChatRoom(Base):
    __tablename__="chat_rooms"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(128),unique=True,index=True,nullable=False)
    description=Column(Text,nullable=True)
    created_at=Column(DateTime(timezone=True),default=datetime.utcnow)
    owner_id=Column(Integer,ForeignKey("users.id"))
    owner=relationship("User",back_populates="rooms")
    messages=relationship("ChatMessage",back_populates="room",cascade="all, delete-orphan")
    uploaded_files=relationship("UploadedFile",back_populates="room",cascade="all, delete-orphan")
    
class ChatMessage(Base):
    __tablename__="chat_messages"
    id=Column(Integer,primary_key=True,index=True)
    room_id=Column(Integer,ForeignKey("chat_rooms.id"))
    user_id=Column(Integer,ForeignKey("users.id"))
    role=Column(Enum(MessageRole),nullable=False)
    content=Column(Text,nullable=False)
    sources=Column(JSON,nullable=True)
    created_at=Column(DateTime(timezone=True),default=datetime.utcnow)
    room=relationship("ChatRoom",back_populates="messages")
    user=relationship("User",back_populates="messages")
    
class UploadedFile(Base):
    __tablename__="uploaded_files"
    id=Column(Integer,primary_key=True,index=True)
    room_id=Column(Integer,ForeignKey("chat_rooms.id"))
    filename=Column(String(255),nullable=False)
    file_type=Column(String(50),nullable=False)
    file_path=Column(String(255),nullable=False)
    status=Column(Enum(FileStatus),default=FileStatus.PROCESSING)
    error_message=Column(Text,nullable=True)
    uploaded_at=Column(DateTime(timezone=True),default=datetime.utcnow)
    room=relationship("ChatRoom",back_populates="uploaded_files")