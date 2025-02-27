from models.user import User
from schemas.user import UserUpdate
from sqlalchemy.orm import Session
import bcrypt
from fastapi import HTTPException

#TODO:添加密码哈希加密 -- [√]
def add_user(new_user: User, db: Session):

    #TODO:检查用户是否存在 -- [√]
    if db.query(User).filter(User.phonenmber_Id == new_user.phonenmber_Id).first():
        raise ValueError("User already exists")
    
    #TODO:检查用户是否为空 -- [√]
    if (new_user!=None):
        #加密密码
        hashed_password = bcrypt.hashpw(new_user.password.encode('utf-8'), bcrypt.gensalt())
        new_user.password = hashed_password.decode('utf-8')

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        raise ValueError("New user cannot be None")


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.phonenmber_Id == user_id).first()

#TODO:ID 和 电话号码不能被修改，绑定 -- [√]
#TODO:完成更新函数，需要创建Up_UserModel--[√]
def update_user(up_user: UserUpdate, user_id: int ,db: Session):
    user = db.query(User).filter(User.phonenmber_Id == user_id).first()
    user.username = up_user.username
    user.password = up_user.password

    hashed_password = bcrypt.hashpw(up_user.password.encode('utf-8'), bcrypt.gensalt())
    user.password = hashed_password.decode('utf-8')
    
    user.email = up_user.email
    db.commit()
    db.refresh(user)
    
    return user

#验证密码
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))