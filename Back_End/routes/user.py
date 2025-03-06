from fastapi import APIRouter, Depends, HTTPException
from model.user import User
from schemas.user import UserCreate, UserRead
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from sqlalchemy.future import select
from crud.user import create_user,get_user_by_id

router = APIRouter(prefix="/user",tags=["USER"])

@router.post("/creat_user", response_model=UserRead)
async def creat_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    #TODO：前置判断

    new_user = await create_user(user, db)
    return new_user

@router.get("/get_user", response_model=UserRead)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    #TODO：前置判断

    user = await get_user_by_id(user_id, db)
    return user

@router.put("/update_user",response_model=UserRead)
async def update_user():
    return