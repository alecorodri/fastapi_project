from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app =  FastAPI(title='Proyecto para reseñar peliculas',
    description='En este proyecto seremos capaces de reseñar peliculas',
    version='1.0.0')



#User Model
class User(BaseModel): #schemas
    id: int
    name: str
    lastName: str
    direction: Optional[str]
    telephone: int
    userCreation: datetime = datetime.now()

@app.post('/ruta2')
def ruta2(user:User):
    user = user.dict()
    print(user)
    return True


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