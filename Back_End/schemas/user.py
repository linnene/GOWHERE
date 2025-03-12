from pydantic import BaseModel
from sqlalchemy import Enum
from sqlalchemy.orm import mapped_column
from schemas.role import RoleType


class UserCreate(BaseModel):
    """
    UserCreate is a Pydantic model that is used to validate
    the data that is sent to the server when creating a new user.
    创建新用户使用的模型
    Example:

{
    "UserId": "18085588360",
    "UserName": "Line",
    "UserPassword": "ioiz73763",
    "UserEmail": "1234@qq.com",
    UserEmailVerified: bool = False,
    "Is_Ban": false
}   
    """

    UserId: str
    UserName: str
    UserPassword: str
    UserEmail: str = None    
    #SAME AS PHONE NUMBER
    UserEmailVerified: bool = False
    Is_Ban: bool = False
    
    role: RoleType = mapped_column(
        Enum(RoleType),
        nullable=False,
        server_default=RoleType.user.name,
        index=True,
    )

    class Config:
        from_attributes = True

class UserRead(BaseModel):
    """
    UserRead is a Pydantic model that is used to validate
    the data that is sent to the server when reading a user.
    读取用户使用的模型
    """
    UserName: str
    UserEmail: str = None    
    #SAME AS PHONE NUMBER
    UserId: str
    Is_Ban: bool 
    UserEmailVerified: bool = False
    
    class Config:
        from_attributes = True

    

class UserUpdate(BaseModel):
    """
    UserUpdate is a Pydantic model that is used to validate
    the data that is sent to the server when updating a user.
    更新用户使用的模型
    """
    
    UserName: str
    UserPassword: str
    UserEmail: str = None    
    Is_Ban: bool
    UserEmailVerified: bool = False

    class Config:
        from_attributes = True