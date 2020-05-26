import os 

class Config:
    SECRET_KEY= os.environ.get("TDL_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI =os.environ.get("TDL_DB_URI")
    MAIL_SERVER="smtp.gmail.com"
    MAIL_PORT= 465
    MAIL_USE_SSL =True
    MAIL_PASSWORD = os.environ.get("TDL_MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER=os.environ.get("TDL_MAIL_USERNAME") 
    MAIL_MAX_EMAILS = None
    MAIL_ASCII_ATTACHMENTS = False

