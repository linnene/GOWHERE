from fastapi import APIRouter,Depends, HTTPException
from database.db import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text

router = APIRouter(tags=["TEST"])


#Test测试节点
@router.get("/Sever_Hearth")
async def Sever_Hearth():
    #TODO：构造返回主机数据函数
    return {"Sever_Hearth": "..."}

#数据库连接Test节点
@router.get("/test-connection")
def test_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "success", "message": "Database connection is working"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))