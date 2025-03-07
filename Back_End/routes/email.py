from fastapi import APIRouter ,BackgroundTasks

from schemas.email import EmailSchema
from fastapi.responses import JSONResponse

from crud.email import send_email
from crud.auth import verify_code

router = APIRouter(prefix="/email",tags=["EMAIL"])

@router.post("/send_template_email")
async def send_template_email(
    email_data: EmailSchema,
    backgroundTasks: BackgroundTasks
    ):

    """
    TODO:mistake --[aiosmtplib.errors.SMTPResponseException: (-1, "Malformed SMTP response line: b'\\x00\\x00\\x00\\x1a\\x00\\x00\\x00\\n'")]
    """

    await send_email(email_data, backgroundTasks)

    return JSONResponse(
        status_code=200, content={"message": "email has been sent"}
    )

@router.post("/verify_code")
async def verify_email_code(code: str, email: str):
    is_valid = await verify_code(code, email)
    if is_valid:
        return JSONResponse(
            status_code=200, content={"message": "Verification successful"}
        )
    else:
        return JSONResponse(
            status_code=400, content={"message": "Invalid verification code"}
        )

