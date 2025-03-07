import redis.asyncio as redis
from fastapi import HTTPException

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# -> None
async def set_value(key: str, value: str):
    
    """
    Save Value in Redis
    """

    await redis_client.set(key, value)

    #TODO: Del this return
    return {"message": f"Key '{key}' set successfully!"}

async def get_value(key: str):
    value = await redis_client.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}

#Update key value
async def update_value(key: str, new_value: str):
    exists = await redis_client.exists(key)
    if not exists:
        raise HTTPException(status_code=404, detail="Key not found")
    await redis_client.set(key, new_value)
    return {"message": f"Key '{key}' updated successfully!", "new_value": new_value}


