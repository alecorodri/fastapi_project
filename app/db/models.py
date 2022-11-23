from app.db.db import Base
from sqlalchemy import Column,Integer,String,Boolean,DateTime
from datetime import datetime


class User(Base):
    __tablename__= "user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    lastName = Column(String)
    address = Column(String)
    telephone = Column(Integer)
    email = Column(String)
    creation = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    status = Column(Boolean)