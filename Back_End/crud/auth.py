from passlib.context import CryptContext
from crud.redis import get_value

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

#TODO： create a verification code for email verification -- [√]
import random
import string

def get_verify_code(length=6):
    characters = string.ascii_letters + string.digits  # 包含大小写字母和数字
    return ''.join(random.choices(characters, k=length))


async def verify_code(code: str, email: str) -> bool:
    stored_code = await get_value(email)
    return code == stored_code

#port:6379
