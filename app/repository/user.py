
from sqlalchemy.orm import Session
from app.db import models

def userCreate(data, db: Session):
    user = data.dict()
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


def getUser(user_id, db: Session):
    data = db.query(models.User).filter(models.User.id == user_id).first()
    if not data:
        return {"answer": "User not found"}
    return data

def deleteUser(user_id, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id)
    if not user.first():
        return {"answer": "User not found"}
    user.delete(synchronize_session= False)
    db.commit()
    return {"answer": "User deleted"}

def getUsers(db: Session):
    data = db.query(models.User).all()
    return 
    
def updateUser(user_id, update_user, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id)
    if not user.first():
        return {"answer": "User not found"}
    user.update(update_user.dict(exclude_unset=True))
    db.commit()
    return {"answer": "User updated"}