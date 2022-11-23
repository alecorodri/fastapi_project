from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5434/fastapi-database"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SesionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)
Base = declarative_base()


def getDb():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()