from fastapi_mail import FastMail, MessageSchema,MessageType
from fastapi import BackgroundTasks

from schemas.email import EmailSchema
from config import conf
from crud.auth import get_verify_code
from crud.redis import set_value

from jinja2 import Template 
from config import conf
import os

template_path = os.path.join(conf.TEMPLATE_FOLDER, "email.html")

async def send_email(
        email_data: EmailSchema ,
        backgroundTasks: BackgroundTasks
        )-> None:

    """
    Use BackgroudTask to do this
    """
    with open(template_path, "r", encoding="utf-8") as file:
        template = Template(file.read())

    # 发送随机的code到email
    Code = get_verify_code()

    await set_value(email_data.recipients[0] , Code)

    email_data.message = "YOUR CODE IS"

    html_content = template.render(name=email_data.name, message= email_data.message,code = Code)

    message = MessageSchema(
        recipients=email_data.recipients,
        subject=email_data.subject,
        body= html_content,
        subtype=MessageType.html,
    )
    
    fm = FastMail(conf)
    backgroundTasks.add_task(fm.send_message ,message)
    
 