from pydantic import BaseModel
from typing import Optional
from datetime import datetime


#User Model
class User(BaseModel): #schemas
    userName: str
    password: str
    name: str
    lastName: str
    address: Optional[str]
    telephone: int
    email: str
    creation: datetime = datetime.now()

class UpdateUser(BaseModel): #schemas
    userName: str = None
    password: str = None
    name: str = None
    lastName: str = None
    address: str = None
    telephone: int = None
    email: str = None
    

class UserId(BaseModel):
    id: int

class ShowUser(BaseModel):
    userName: str
    name: str
    lastName: str
    email: str
    class Config():
        orm_mode = True