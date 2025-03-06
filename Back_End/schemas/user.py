from pydantic import BaseModel


class UserCreate(BaseModel):
    """
    UserCreate is a Pydantic model that is used to validate
    the data that is sent to the server when creating a new user.
    创建新用户使用的模型
    """

    UserName: str
    UserPassword: str
    UserEmail: str = None    
    #SAME AS PHONE NUMBER
    UserId: int
    Is_Ban: bool = True

class UserRead(BaseModel):
    """
    UserRead is a Pydantic model that is used to validate
    the data that is sent to the server when reading a user.
    读取用户使用的模型
    """
    UserName: str
    UserEmail: str = None    
    #SAME AS PHONE NUMBER
    UserId: int
    Is_Ban: bool = True

class UserUpdate(BaseModel):
    """
    UserUpdate is a Pydantic model that is used to validate
    the data that is sent to the server when updating a user.
    更新用户使用的模型
    """
    
    UserName: str
    UserPassword: str
    UserEmail: str = None    
    UserName: bool = True
    Is_Ban: bool = True
