
from fastapi import APIRouter,Depends
from app.schemas import User, UserId, ShowUser
from app.db.db import getDb
from sqlalchemy.orm import Session
from app.db import models
from typing import List
router = APIRouter(
    prefix= "/user",
    tags=["Users"]
)

@router.get('/',response_model=List[ShowUser])
def getUsers(db: Session = Depends(getDb)):
    users = db.query(models.User).all()
    return users

@router.post('/')
def userCreate(user:User, db: Session = Depends(getDb)):
    user = user.dict()
    newUser = models.User(
        userName = user["userName"],
        password = user["password"],
        name = user["name"],
        lastName = user["lastName"],
        address = user["address"],
        telephone = user["telephone"],
        email = user["email"],
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return {"answer" : "User created"}

@router.get('/{user_id}',response_model=ShowUser)
def getUser(user_id:int, db: Session = Depends(getDb)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return {"answer": "User not found"}
    return user


@router.post('/get_user')
def getUser2(user_id:UserId):
    for user in users:
        if user["id"] == user_id.id:
            return {"user": user}
    return {"answer": "User not found"}

@router.delete('/{user_id}')
def deleteUser(user_id:int):
    for index,user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return {"answer": "User deleted"}
    return {"answer": "User not found"}

@router.put('/{user_id}')
def updateUser(user_id: int, update_user: User):
    for index,user in enumerate(users):
        if user["id"] == user_id:
            users[index]["id"] = update_user.dict()["id"]
            users[index]["name"] = update_user.dict()["name"]
            users[index]["lastName"] = update_user.dict()["lastName"]
            users[index]["address"] = update_user.dict()["address"]
            users[index]["telephone"] = update_user.dict()["telephone"]
            return {"answer": "User updated"}
    return {"answer": "User not updated"}