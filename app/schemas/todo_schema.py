from pydantic import BaseModel
from typing import Optional

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class TodoOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    class Config:
        orm_mode = True
