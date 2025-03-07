from fastapi import APIRouter 

from schemas.email import EmailSchema
from config import conf
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema,MessageType

router = APIRouter(prefix="/email",tags=["EMAIL"])

@router.post("/send_template_email")
async def send_template_email(email_data: EmailSchema):
    """
    TODO:mistake --[aiosmtplib.errors.SMTPResponseException: (-1, "Malformed SMTP response line: b'\\x00\\x00\\x00\\x1a\\x00\\x00\\x00\\n'")]
    """
    with open("D:/GOWHERE/Back_End/templates/email/email.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    message = MessageSchema(
        recipients=email_data.recipients,
        subject=email_data.subject,
        body= html_content,
        subtype=MessageType.html,
    )
    
    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(
        status_code=200, content={"message": "email has been sent"}
    )

