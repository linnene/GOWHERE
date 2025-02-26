from fastapi import FastAPI, Depends, HTTPException
from database.db import get_db,engine,Base
from sqlalchemy.orm import Session
from sqlalchemy import text
from Routes.user import router as user_router


app = FastAPI()
app.include_router(user_router, prefix="/user", tags=["USER"])

Base.metadata.create_all(bind=engine)



#Test测试节点
@app.get("/Sever_Hearth")
async def Sever_Hearth():
    return {"Sever_Hearth": "..."}
#数据库连接Test节点
@app.get("/test-connection")
def test_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "success", "message": "Database connection is working"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))