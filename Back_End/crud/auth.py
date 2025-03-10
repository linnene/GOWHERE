from fastapi import  HTTPException, status
from passlib.context import CryptContext
import datetime
import random
import string
import jwt

from crud.redis import get_value
from model.user import User
from config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Hash the password 哈希密码存储
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


#TODO： create a verification code for email verification -- [√]
#创建邮件验证码
def get_verify_code(length=6):
    characters = string.ascii_letters + string.digits  # 包含大小写字母和数字
    return ''.join(random.choices(characters, k=length))

#Verificate for email code
async def verify_code(code: str, email: str) -> bool:
    stored_code = await get_value(email)
    return code == stored_code


#Create a JWT 短期 token
def encode_token(user: User) -> str:
        """Create and return a JTW token."""
        try:
            payload = {
                "sub": user.UserId,
                
                #TODO:过期时间，检验时记得校验
                "exp": datetime.datetime.now(tz=datetime.timezone.utc)
                + datetime.timedelta(
                    minutes= settings.access_token_expire_minutes
                ),
            }
            return jwt.encode(
                payload, settings.secret_key, algorithm="HS256"
            )
        
        except (jwt.PyJWTError, AttributeError) as exc:
            # log the exception
            raise HTTPException(
                status.HTTP_401_UNAUTHORIZED
            ) from exc


#Create a JWT 长期 refresh
def encode_refresh_token(user: User) -> str:
        """Create and return a JTW token."""
        try:
            payload = {
                "sub": user.UserId,
                "exp": datetime.datetime.now(tz=datetime.timezone.utc)
                + datetime.timedelta(minutes= settings.refresh_token_expire_minutes),
                "typ": "refresh",
            }
            return jwt.encode(
                payload, settings.secret_key, algorithm="HS256"
            )
        except (jwt.PyJWTError, AttributeError) as exc:
            # log the exception
            raise HTTPException(
                status.HTTP_401_UNAUTHORIZED
            ) from exc
