from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate , UserRead ,UserUpdate, UserLogin
from crud.user import add_user,get_user,update_user,verify_password
from database.db import get_db

router = APIRouter()


@router.post("/createuser", response_model=UserRead)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):

    #TODO:解决user.dict()问题 -- [√]
    #TODO:完善报错 -- [√]
    try:
        new_user = add_user(User(**user.model_dump()), db)
    except HTTPException as e:
        if e.status_code == 400:
            raise HTTPException(status_code=400, detail="User with this phone number already exists")
        else:
            raise e
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return new_user


@router.get("/querUser/{user_id}", response_model=UserRead )
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/updateUser/{user_id}", response_model=UserRead)
async def update_user_info(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(user, user_id, db)
    return updated_user

@router.post("/login", response_model=UserRead, description="Login user")
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.phonenmber_Id == user.phonenmber_Id).first()
    
    if db_user is None or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid phone number or password")
    return db_user