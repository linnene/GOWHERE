from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends 
from database.db import get_db
from typing import Annotated

from crud.auth import encode_token ,encode_refresh_token
from crud.user import get_user_by_id

router = APIRouter(prefix="/auth",tags=["AUTH"])

@router.post("/token")
async def get_token(user_id: str, db: Annotated[AsyncSession, Depends(get_db)]):
    """
    Test-25/3/8 -- [Complet]-[Success]
    """
    user = await get_user_by_id(user_id, db)
    #TODO:安全性问题
    
    if user.UserPassword :
        return {"token":encode_token(user),"refresh_token":encode_refresh_token(user)}
    else:
        return {"message":"password is wrong or None"}
        

    