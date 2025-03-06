from fastapi import APIRouter
from routes import user

api_route = APIRouter(prefix="/v1",tags=["V1"])

api_route.include_router(user.router)