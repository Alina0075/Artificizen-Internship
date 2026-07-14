from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from oauth2 import get_current_user
from models import Task
from schema import TaskCreate, TaskResponse

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/",response_model=TaskResponse)
def create_task(task:TaskCreate, db: Session=Depends(get_db),current_user=Depends(get_current_user)):
    new_task=Task(**task.model_dump(),owner_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/",response_model=list[TaskResponse])
def get_tasks(status:str=None, db:Session = Depends(get_db), current_user=Depends(get_current_user)):
    query=db.query(Task).filter(Task.owner_id==current_user.id)
    if status:
        query=query.filter(Task.status==status)
    return query.all()
    
@router.get("/{task_id}",response_model=TaskResponse)
def get_single_task(task_id:int, db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    task=db.query(Task).filter(Task.id==task_id,Task.owner_id==current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}",response_model=TaskResponse)
def update_task(task_id:int,updated:TaskCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    task=db.query(Task).filter(Task.id==task_id,Task.owner_id==current_user.id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    for key,value in updated.model_dump().items():
        setattr(task,key,value)
    db.commit()
    db.refresh(task)
    
    return task

@router.delete("/{task_id}")
def delete_task(task_id:int, db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    task=db.query(Task).filter(Task.id==task_id, Task.owner_id==current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return{"message": "Task deleted successfully"}

     
    