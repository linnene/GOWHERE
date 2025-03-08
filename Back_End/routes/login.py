from fastapi import APIRouter, Depends ,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from typing import Annotated

from crud.user import get_user_by_id
from crud.auth import verify_password
from schemas.user import UserRead

router = APIRouter(prefix="/login", tags=["LOGIN"])


@router.post("/login",response_model = UserRead)
async def login(
    user_id: str,
    password :str,
    db: Annotated[AsyncSession , Depends(get_db)]
    ):
    """
    Test-25/3/8 -- [Complet]-[Success]
    """
    if (user_id == None or password == None):
        raise HTTPException(status_code=400, detail="Password or User_id cannot be empty")
    
    user = await get_user_by_id(user_id, db)
    try:
        if verify_password(password, user.UserPassword):
            return user
        else:
            raise HTTPException(status_code=401, detail="Incorrect password")
        
    except HTTPException as e:
        raise HTTPException(status_code=401, detail="Incorrect password")
    
@router.post("/logout")
async def logout():
    return {"message":"logout success"}