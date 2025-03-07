from fastapi_mail import ConnectionConfig
from pathlib import Path



class Settings:
    # DB connect settings
    
    DB_USERNAME = "root"
    DB_PASSWORD ="IOIZ73763jfl"
    DB_HOST = "localhost"
    DB_PORT = 3306
    DB_NAME = "gowhere"

    #Email settings
    mail_username: str = "teadark@qq.com"
    mail_password: str = "nrubibousefkdgjc"  
    mail_from: str = "2691234891@qq.com"
    mail_port: int = 465
    mail_server: str = "smtp.qq.com"
    mail_from_name: str = "gowhere"
    mail_starttls: bool = False
    mail_ssl_tls: bool = True
    mail_use_credentials: bool = True
    mail_validate_certs: bool = False


settings = Settings()

#Fastmail settings

conf = ConnectionConfig(
            MAIL_USERNAME= settings.mail_username,
            MAIL_PASSWORD= settings.mail_password,
            MAIL_FROM= settings.mail_from,
            MAIL_PORT= settings.mail_port,
            MAIL_SERVER= settings.mail_server,
            MAIL_FROM_NAME= settings.mail_from_name,
            MAIL_STARTTLS= settings.mail_starttls,
            MAIL_SSL_TLS= settings.mail_ssl_tls,
            USE_CREDENTIALS= settings.mail_use_credentials,
            VALIDATE_CERTS= settings.mail_validate_certs,
            TEMPLATE_FOLDER= Path("D:/GOWHERE/Back_End/templates/email/"),
            SUPPRESS_SEND = 0 
        )
