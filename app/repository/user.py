
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


def getUser(user_id,db: Session):
    data = db.query(models.User).filter(models.User.id == user_id).first()
    if not data:
        return {"answer": "User not found"}
    return data