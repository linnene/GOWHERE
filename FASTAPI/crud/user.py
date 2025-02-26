from models.user import User
from schemas.user import UserUpdate
from sqlalchemy.orm import Session

def add_user(new_user: User, db: Session):
    if new_user is not None:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        raise ValueError("New user cannot be None")

#TODO:完成更新函数，需要创建Up_UserModel--[√]
#TODO:ID 和 电话号码不能被修改，绑定

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.phonenmber_Id == user_id).first()


def update_user(up_user: UserUpdate, user_id: int,db: Session):
    user = db.query(User).filter(User.phonenmber_Id == user_id).first()
    user.username = up_user.username
    user.password = up_user.password
    user.email = up_user.email
    db.commit()
    db.refresh(user)
    
    return user