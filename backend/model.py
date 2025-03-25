from pydantic import BaseModel
from typing import Optional


class ToDo(BaseModel):
    title :str
    description : Optional[str] = None
    completed : bool = False
    priority : Optional[int] = 1
    due_date : Optional[str] = None

    class Config:
        orm_mode = True


class User(BaseModel):
    name : Optional[str] = None
    username : str
    password : str

