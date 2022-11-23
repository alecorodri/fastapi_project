from fastapi import FastAPI
import uvicorn
from app.routers import user_router
from app.db.db import Base,engine

def createTables():
    Base.metadata.create_all(bind=engine)
createTables()

app =  FastAPI(title='FastAPI Demo',
    description='Learn FastAPI',
    version='1.0.0')

app.include_router(user_router.router)



# @app.on_event('startup')
# def startUp():
#     print('Iniciando server')

# @app.on_event('shutdown')
# def shutDown():
#     print('Finalizando server')


if  __name__=="__main__":
        uvicorn.run("main:app",port = 8000,reload = True)