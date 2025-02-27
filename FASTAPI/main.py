from fastapi import FastAPI
from database.db import engine, Base
from Routes.routes import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api", tags=["API"])

#检查表项是否创建
Base.metadata.create_all(bind=engine)