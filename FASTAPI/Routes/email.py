from fastapi import APIRouter
from crud.email import generate_code


router = APIRouter(tags=["EMAIL"])


@router.post("/send-email")
async def ver_email(email: str,):
    return