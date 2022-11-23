from fastapi import FastAPI
import uvicorn


app =  FastAPI(title='FastAPI Demo',
    description='Learn FastAPI',
    version='1.0.0')


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