import bcrypt


#验证密码
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
def creat_token():
    pass

def verify_token(token: str) -> bool:
    pass