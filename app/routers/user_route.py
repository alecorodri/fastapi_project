from fastapi import APIRouter


router = APIRouter(
    prefix= "/user",
    tags=["Users"]
)

@router.get('/user')
def getUsers():
    return users

@router.post('/user')
def userCreate(user:User):
    user = user.dict()
    users.append(user)
    return {"answer" : "User created"}

@router.post('/user/{user_id}')
def getUsers(user_id:int):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return {"answer": "User not found"}


@router.post('/get_user')
def getUser2(user_id:UserId):
    for user in users:
        if user["id"] == user_id.id:
            return {"user": user}
    return {"answer": "User not found"}

@router.delete('/user/{user_id}')
def deleteUser(user_id:int):
    for index,user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return {"answer": "User deleted"}
    return {"answer": "User not found"}

@router.put('/user/{user_id}')
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