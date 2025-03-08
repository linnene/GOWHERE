from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends 
from database.db import get_db
from typing import Annotated

from schemas.user import UserCreate, UserRead, UserUpdate
from crud.user import create_user,get_user_by_id,reflush_user

router = APIRouter(prefix="/user",tags=["USER"])

@router.post("/creat_user", response_model=UserRead)
async def creat_user(
    user: UserCreate, 
    db: Annotated[AsyncSession , Depends(get_db)]
    ):
    """
    Test-25/3/8 -- [Complet]-[Success]
    """
    #TODO：前置判断

    new_user = await create_user(user, db)
    return new_user

@router.get("/get_user", response_model=UserRead)
async def get_user(
    user_id: str, 
    db: Annotated[AsyncSession , Depends(get_db)]
    ):
    """
    Test-25/3/8 -- [Complet]-[Success]
    """

    #TODO：前置判断

    user = await get_user_by_id(user_id, db)
    return user

@router.put("/update_user", response_model=UserRead)
async def update_user(
    user_id: str,
    new_user: UserUpdate,
    db: Annotated[AsyncSession , Depends(get_db)]
    ):
    
    #BUG: 使用接口Updateuser无法找到用户
    #TODO： 更新用户信息

    user = await reflush_user(user_id, new_user, db)
    return user

