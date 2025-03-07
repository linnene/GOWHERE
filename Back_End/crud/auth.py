from passlib.context import CryptContext

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

#port:6379