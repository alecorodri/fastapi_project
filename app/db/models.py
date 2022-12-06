from app.db.db import Base
from sqlalchemy import Column,Integer,String,Boolean,DateTime
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__= "user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    userName = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    lastName = Column(String)
    address = Column(String)
    telephone = Column(Integer)
    email = Column(String, unique=True)
    creation = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    status = Column(Boolean,default=False)
    sale = relationship("sale",backref="user",cascade="delete,merge")

class Sale(Base):
    __tablename__= "sale"
    id = Column(Integer,primary_key=True,autoincrement=True)
    userId = Column(Integer,ForeignKey("user.id",ondelete="CASCADE"))
    sale = Column(Integer)
    productSale = Column(Integer)