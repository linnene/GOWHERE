from pydantic import BaseModel

#用户创建模型
class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    phonenmber_Id: int

#用户更新模型
class UserUpdate(BaseModel):
    username: str
    password: str
    email: str

#用户可读模型
class UserRead(BaseModel):
    username: str
    email: str
    phonenmber_Id: str

class UserLogin(BaseModel):
    phonenmber_Id: int
    password: str
    