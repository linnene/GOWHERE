from sqlalchemy import Column, String
from database.db import Base
#from .enums import RoleType
from pydantic import BaseModel

class User(Base):
    __tablename__ = 'USERS'
    
    username: str = Column(String(50), nullable=False)
    #密码存储为哈希
    password: str = Column(String(200), nullable=False)
    #邮箱可为空
    email: str = Column(String(50), nullable=True)

    # 使用手机号作为主键
    phonenmber_Id: int = Column(String(50), primary_key=True, nullable=False)

