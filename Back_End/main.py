from fastapi import FastAPI
from database.db import engine
from contextlib import asynccontextmanager
from model.base import Base
from routes.route import api_route


#-----------在导入模块之后------------
app = FastAPI()
 
# Create the database tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield  
    await engine.dispose()
#-----------其他操作之前--------------


app = FastAPI(lifespan=lifespan)  

#注意位置，需要在life span之后
app.include_router(api_route, prefix="/api")