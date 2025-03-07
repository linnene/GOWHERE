from fastapi import APIRouter,HTTPException
from crud.redis import redis_client
from pydantic import EmailStr
from crud.auth import verify_code
router = APIRouter(tags=["TEST"])

# TEST REDIS connert Success

@router.get("/ping")
async def ping():
    try:
        pong = await redis_client.ping()
        return {"status": "Redis Connected", "ping": pong}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Redis connection error: {e}")

@router.get("/ver_code")
async def ver_code(email: EmailStr,code: str) -> bool:
    """
    Verify the code from redis
    """
    return await verify_code(code=code,email=email)