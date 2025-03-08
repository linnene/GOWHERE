from fastapi import APIRouter
from routes import user, login, email, test, auth

api_route = APIRouter(prefix="/v1",tags=["V1"])

api_route.include_router(user.router)
api_route.include_router(login.router)
api_route.include_router(email.router)
api_route.include_router(test.router)
api_route.include_router(auth.router)
