
from fastapi import APIRouter,Depends
from app.schemas import User, UserId, ShowUser, UpdateUser
from app.db.db import getDb
from sqlalchemy.orm import Session
from app.db import models
from typing import List
router = APIRouter(
    prefix= "/user",
    tags=["Users"]
)
users = []
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
def deleteUser(user_id:int, db: Session = Depends(getDb)):
    user = db.query(models.User).filter(models.User.id == user_id)
    if not user.first():
        return {"answer": "User not found"}
    user.delete(synchronize_session= False)
    db.commit()

    return {"answer": "User deleted"}

@router.patch('/{user_id}')
def updateUser(user_id: int, update_user: UpdateUser, db: Session = Depends(getDb)):
    user = db.query(models.User).filter(models.User.id == user_id)
    if not user.first():
        return {"answer": "User not found"}
    user.update(update_user.dict(exclude_unset=True))
    db.commit()
    return {"answer": "User updated"}