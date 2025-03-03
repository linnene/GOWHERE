from pydantic import BaseModel

class send_email(BaseModel):
    to_emails: list[str]

#邮箱验证码
class auth_email(send_email):
    #过期时间
    Exp_time: int

