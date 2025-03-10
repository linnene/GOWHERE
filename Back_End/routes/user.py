from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends ,HTTPException
from database.db import get_db
from typing import Annotated,Union

from schemas.user import UserCreate, UserRead, UserUpdate
from crud.user import create_user,get_user_by_id,reflush_user

router = APIRouter(prefix="/user",tags=["USER"])

@router.post(
"/creat_user", 
#有可能阻断返回的错误值
response_model=UserRead,
name="Create a new user"
)
async def creat_user(
    user: UserCreate, 
    db: Annotated[AsyncSession , Depends(get_db)],
    ):
    
    """
    Description:
    1. 通过用户信息创建用户
    2. 如果用户已经注册，则返回错误信息
    3. 如果用户密码为空，则返回错误信息
    4. 返回UserRead信息

    Test-25/3/8 -- [Complet]-[Success]
    Change-25/3/10 -- [Complet]-[Success]

    """

    #检查用户密码是否为空
    if user.UserPassword != None and user.UserPassword != "string":
        #创建用户
        new_user = await create_user(user, db)
    else:
        return {"message":"password can't be None"}
    
    return UserRead.model_validate(new_user)

@router.get(
"/get_user", 
# response_model=UserRead
)

async def get_user(
    user_id: str, 
    db: Annotated[AsyncSession , Depends(get_db)]
    ):

    """
    安全性问题
    将验证查询角色role
    Test-25/3/8 -- [Complet]-[Success]
    """

    #TODO：前置判断

    user = await get_user_by_id(user_id, db)
    return user

@router.put(
"/update_user",
# response_model= UserRead
)
async def update_user(
    user_id: str,
    new_user: UserUpdate,
    db: Annotated[AsyncSession , Depends(get_db)]
    ):
    
    #BUG: 使用接口Updateuser无法找到用户
    #TODO： 更新用户信息

    user = await reflush_user(user_id, new_user, db)
    return user

