from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app =  FastAPI(title='FastAPI Demo',
    description='Learn FastAPI',
    version='1.0.0')

users = []



#User Model
class User(BaseModel): #schemas
    id: int
    name: str
    lastName: str
    direction: Optional[str]
    telephone: int
    userCreation: datetime = datetime.now()

class UserId(BaseModel):
    id: int

@app.get('/user')
def getUsers():
    return users

@app.post('/user')
def userCreate(user:User):
    user = user.dict()
    users.append(user)
    return {"answer" : "User created"}

@app.post('/user/{user_id}')
def getUsers(user_id:int):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return {"answer": "User not found"}


@app.post('/get_user')
def getUser2(user_id:UserId):
    for user in users:
        if user["id"] == user_id.id:
            return {"user": user}
    return {"answer": "User not found"}

@app.delete('/user/{user_id}')
def deleteUser(user_id:int):
    for index,user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return {"answer": "User deleted"}
    return {"answer": "User not found"}

@app.put('/user/{user_id}')
def updateUser(user_id: int, update_user: User):
    for index,user in enumerate(users):
        if user["id"] == user_id:
            users[index]["id"] = update_user.dict()["id"]
            users[index]["name"] = update_user.dict()["name"]
            users[index]["lastName"] = update_user.dict()["lastName"]
            users[index]["direction"] = update_user.dict()["direction"]
            users[index]["telephone"] = update_user.dict()["telephone"]
            return {"answer": "User updated"}
    return {"answer": "User not updated"}

@app.on_event('startup')
def startUp():
    print('Iniciando server')

@app.on_event('shutdown')
def shutDown():
    print('Finalizando server')

@app.get('/')
async def index():
    return 'Hello World'

@app.get('/about')
async def about():
    return 'About Page'


if  __name__=="__main__":
        uvicorn.run("main:app",port = 8000,reload = True)