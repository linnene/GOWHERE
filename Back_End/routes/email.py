from fastapi import APIRouter ,BackgroundTasks

from schemas.email import EmailSchema
from fastapi.responses import JSONResponse

from crud.email import send_email
router = APIRouter(prefix="/email",tags=["EMAIL"])

@router.post("/send_template_email")
async def send_template_email(
    email_data: EmailSchema,
    backgroundTasks: BackgroundTasks
    ):

    """
    TODO:mistake --[aiosmtplib.errors.SMTPResponseException: (-1, "Malformed SMTP response line: b'\\x00\\x00\\x00\\x1a\\x00\\x00\\x00\\n'")]
    """

    await send_email(email_data,backgroundTasks)

    return JSONResponse(
        status_code=200, content={"message": "email has been sent"}
    )

