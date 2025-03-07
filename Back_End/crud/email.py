from fastapi_mail import FastMail, MessageSchema,MessageType
from fastapi import BackgroundTasks

from schemas.email import EmailSchema
from config import conf
from crud.auth import get_verify_code

from jinja2 import Template 

async def send_email(
        email_data: EmailSchema ,
        backgroundTasks: BackgroundTasks
        )-> None:

    """
    Use BackgroudTask to do this
    """

    with open("D:/GOWHERE/Back_End/templates/email/email.html", "r", encoding="utf-8") as file:
        template = Template(file.read())

    # 发送随机的code到email
    code = get_verify_code()
    email_data.message = f"YOUR CODE IS {code}"

    html_content = template.render(name=email_data.name, message= email_data.message)

    message = MessageSchema(
        recipients=email_data.recipients,
        subject=email_data.subject,
        body= html_content,
        subtype=MessageType.html,
    )
    
    fm = FastMail(conf)
    backgroundTasks.add_task(fm.send_message ,message)