from pydantic import BaseModel, EmailStr


class EmailSchema(BaseModel):
    recipients: list[EmailStr]
    subject: str = "GOWHERE"
    name: str = "GOWHERE"
    message: str = "This is the test email content"

# Compare this snippet from Back_End/schemas/email.py:


class EmailTemplateSchema(BaseModel):
    recipients: list[EmailStr]
    subject: str
    template_name: str
