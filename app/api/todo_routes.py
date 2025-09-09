from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.todo_schema import TodoCreate, TodoUpdate, TodoOut
from app.database import models
from app.api.deps import get_db, get_current_user

router = APIRouter(prefix="/todos", tags=["todos"])

# Create todo
@router.post("/", response_model=TodoOut)
def create(todo: TodoCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_todo = models.Todo(
        title=todo.title,
        description=todo.description,
        user_id=user.id
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# List all todos for logged-in user
@router.get("/", response_model=List[TodoOut])
def list_todos(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.Todo).filter(models.Todo.user_id == user.id).all()

# Get single todo
@router.get("/{todo_id}", response_model=TodoOut)
def get_one(todo_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.user_id == user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# Update todo
@router.put("/{todo_id}", response_model=TodoOut)
def update(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.user_id == user.id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    for key, value in todo.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo

# Delete todo
@router.delete("/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.user_id == user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"detail": "Todo deleted"}
