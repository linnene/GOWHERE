from fastapi import APIRouter

from Routes import user, login, test

api_router = APIRouter(prefix="/v1")

api_router.include_router(user.router)
api_router.include_router(login.router)
api_router.include_router(test.router)

