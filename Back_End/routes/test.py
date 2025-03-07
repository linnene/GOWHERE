from fastapi import APIRouter,HTTPException
from crud.redis import redis_client

router = APIRouter(tags=["TEST"])

# TEST REDIS connert Success

@router.get("/ping")
async def ping():
    try:
        pong = await redis_client.ping()
        return {"status": "Redis Connected", "ping": pong}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Redis connection error: {e}")
