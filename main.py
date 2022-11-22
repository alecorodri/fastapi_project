from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


app =  FastAPI(title='Proyecto para reseñar peliculas',
    description='En este proyecto seremos capaces de reseñar peliculas',
    version='1.0.0')

@app.on_event('startup')
def startUp():
    print('Iniciando server')

@app.on_event('shutdown')
def shutDown():
    print('Finalizando server')

@app.post('/ruta2')
def ruta2(user):
    print(user)
    return True

@app.get('/')
async def index():
    return 'Hello World'

@app.get('/about')
async def about():
    return 'About Page'