from model.base import Base
from sqlalchemy import String, Column, Integer,Boolean

class User(Base):
    __tablename__ = "user"

    UserId = Column(Integer, primary_key=True, index=True)
    UserEmail = Column(String(255), index=True)

    # hashed_password
    UserPassword = Column(String(255), index=True)
    UserName = Column(String(255), index=True)  
    
    #is BAN
    Is_Ban = Column(Boolean, default=1)