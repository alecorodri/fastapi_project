
from fastapi import APIRouter,Depends
from app.schemas import User, UserId, ShowUser, UpdateUser
from app.db.db import getDb
from sqlalchemy.orm import Session
from app.db import models
from typing import List
from app.repository import user


router = APIRouter(
    prefix= "/user",
    tags=["Users"]
)
users = []
@router.get('/',response_model=List[ShowUser])
def getUsers(db: Session = Depends(getDb)):
    data = user.getUsers(db)
    return data

@router.post('/')
def userCreate(data :User, db: Session = Depends(getDb)):
    user.userCreate(data, db)
    return {"answer" : "User created"}

@router.get('/{user_id}',response_model=ShowUser)
def getUser(user_id:int, db: Session = Depends(getDb)):
    data = user.getUser(user_id, db)
    return data


@router.post('/get_user')
def getUser2(user_id:UserId):
    for user in users:
        if user["id"] == user_id.id:
            return {"user": user}
    return {"answer": "User not found"}

@router.delete('/{user_id}')
def deleteUser(user_id:int, db: Session = Depends(getDb)):
    res = user.deleteUser(user_id, db)
    return res

@router.patch('/{user_id}')
def updateUser(user_id: int, update_user: UpdateUser, db: Session = Depends(getDb)):
    res = user.updateUser(user_id,updateUser,db)
    return res