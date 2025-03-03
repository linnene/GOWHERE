import random

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from schemas.email  import auth_email

#修改为数字字母混合验证码
def generate_code():
    return str(random.randint(100000, 999999))

#发送邮件函数
def send_email(auth_email: auth_email):
    
    #TODO:之后移动到配置文件中
    from_email = "teadarkline@gmail.com"
    from_password = "cdnu ogrj gxvx oubq"

    #TODO:修改为Gmail SMTP地址--[√]
    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.starttls()

    for  to_email in auth_email.to_emails :
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "Your Verification Code"

        body = f"Your verification code is 114514"
        msg.attach(MIMEText(body, 'plain'))


        server.login(from_email, from_password)

        text = msg.as_string()

        server.sendmail(from_email, to_email, text)
    server.quit()