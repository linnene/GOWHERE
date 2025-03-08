from model.base import Base
from sqlalchemy import String, Column, Boolean

class User(Base):
    __tablename__ = "user"

    UserId = Column(String(255), primary_key=True,nullable=False, index=True)
    UserEmail = Column(String(255), index=True)

    # hashed_password
    UserPassword = Column(String(255), index=False)
    UserName = Column(String(255), index=True)  

    #is email verified
    UserEmailVerified = Column(Boolean, default=False)
    
    #is BAN
    Is_Ban = Column(Boolean, default=1)