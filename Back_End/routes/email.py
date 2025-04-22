from fastapi import APIRouter ,BackgroundTasks,Depends

from schemas.email import EmailSchema
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated


from crud.email import send_email
from crud.auth import verify_code
from crud.user import set_user_emaliVer
from database.db import get_db

router = APIRouter(prefix="/email",tags=["EMAIL"])

@router.post(
        "/send_template_email",
        name="Send ver_Code Email to Email"
)
async def send_template_email(
    email_data: EmailSchema,
    backgroundTasks: BackgroundTasks
):

    """
    Test-25/3/8 -- [Complet]-[Success (?)]
    BUG :mistake --[aiosmtplib.errors.SMTPResponseException: (-1, "Malformed SMTP response line: b'\\x00\\x00\\x00\\x1a\\x00\\x00\\x00\\n'")]
    TODO：更换 qq SMTP ,使用hotemail SMTP
    """

    await send_email(email_data, backgroundTasks)

    return JSONResponse(
        status_code=200, content={"message": "email has been sent"}
    )


@router.post("/verify_code")
async def verify_email_code(
    code: str, 
    email: str, 
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    Test-25/3/8 -- [Complet]-[Success]

    """
    async with db.begin():  # 开始事务
        is_valid = await verify_code(code, email)
        if is_valid:
            await set_user_emaliVer(email, db)
            return JSONResponse(
                status_code=200, content={"message": "Verification successful"}
            )
        else:
            return JSONResponse(
                status_code=400, content={"message": "Invalid verification code"}
            )