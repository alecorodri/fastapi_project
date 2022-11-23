from pydantic import BaseModel
from typing import Optional
from datetime import datetime


#User Model
class User(BaseModel): #schemas
    id: int
    name: str
    lastName: str
    address: Optional[str]
    telephone: int
    email: str
    creation: datetime = datetime.now()

class UserId(BaseModel):
    id: int