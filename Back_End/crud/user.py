from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from model.user import User
from schemas.user import UserCreate
from fastapi import HTTPException

async def create_user(user: UserCreate, db: AsyncSession) -> User:
    """
    有关创建一个新的用户，现在的用户ID又数据库自己创建，
    之后会将ID改为PhoneNumber将账号和手机号绑定
    TODO：修改 {User} 中的 ID 表项
    """
    async with db.begin():  # 开启事务
        result = await db.execute(select(User).filter(User.UserId == user.UserId))
        existing_user = result.scalars().first()
        if existing_user:
            raise HTTPException(status_code=400, detail="User already registered")
        new_user = User(**user.model_dump())
        db.add(new_user)
        await db.flush()

    # TODO:如果数据库字段不会自动填充（如 created_at），可以不 refresh()，提升性能。
    # await db.refresh(new_user)
    return new_user

async def get_user_by_id(user_id: int, db: AsyncSession):
    async with db.begin():
        result = await db.execute(select(User).filter(User.UserId == user_id))
        user = result.scalars().first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user