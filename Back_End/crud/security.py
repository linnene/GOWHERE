from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Annotated
import jwt

from crud.user import get_user_by_id
from database.db import get_db
from model.user import User
from config import settings

#自动获取标头Token
bearer = HTTPBearer(auto_error=False)

#通过JWT令牌获取用户信息，用于自动注入
async def get_jwt_user(
    request: Request,
    db: Annotated[AsyncSession , Depends(get_db)],
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer),
) -> Optional[User]:
    
    if not credentials:
        return None

    try:
        # Decode and validate the token
        payload = jwt.decode(
            credentials.credentials,
            settings.secret_key,
            algorithms=["HS256"],
            options={"verify_sub": False ,"verify_exp": True},
        )

        if payload["exp"] < payload["iat"]:
            raise

        user_data = await get_user_by_id(payload["sub"], db)

        # Check user validity
        if (
            not user_data
            or not bool(user_data.UserEmailVerified)
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        # Store user in request state
        request.state.user = user_data

    except jwt.ExpiredSignatureError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        ) from exc
    
    except jwt.InvalidTokenError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        ) from exc
    else:
        return user_data
    
oauth2_schema = get_jwt_user

#自动获取当前访问用户
async def get_current_user(
    jwt_user: Optional[User] = Depends(oauth2_schema),
) -> User:
    
    if jwt_user:
        return jwt_user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated. Use either JWT token or API key.",
            headers={"WWW-Authenticate": "Bearer or ApiKey"},
        )