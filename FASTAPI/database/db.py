from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#TODO：将数据库连接方式改为异步async

#TODO：Move to config file
DATABASE_URL = "mysql+pymysql://root:IOIZ73763jfl@127.0.0.1:3306/gowhere"  

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Create connection to database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()