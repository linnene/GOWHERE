from config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DATABASE_URL = f"mysql+asyncmy://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"


# 创建异步引擎
engine = create_async_engine(DATABASE_URL, echo=False)

# 创建异步 Session 类
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

#获取数据库Session
async def get_db():
    session = AsyncSessionLocal()
    try:
        yield session
    finally:
        await session.close()

