from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User
from database.db import get_db
from schemas.user import UserRead, UserLogin
from crud.auth import verify_password

login = APIRouter()

@login.post("/login", response_model=UserRead, description="Login user")
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.phonenmber_Id == user.phonenmber_Id).first()
    
    if db_user is None or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid phone number or password")
    return db_user