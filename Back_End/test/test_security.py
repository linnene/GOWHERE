import pytest
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from unittest.mock import AsyncMock, patch

from crud.security import get_current_user, oauth2_schema
from model.user import User

app = FastAPI()

# 创建一个测试端点来测试 get_current_user 函数
@app.get("/test-current-user", response_model=User)
async def test_current_user(current_user: User = Depends(get_current_user)):
    return current_user

# 创建一个测试客户端
client = TestClient(app)

# 模拟数据库会话
@pytest.fixture
def db_session():
    return AsyncMock(AsyncSession)

# 模拟用户数据
@pytest.fixture
def mock_user():
    return User(
        UserId="test_user_id",
        UserName="test_user",
        UserEmail="test_user@example.com",
        UserEmailVerified=True,
        Is_Ban=False,
    )

# 测试成功获取当前用户
@patch("crud.security.get_user_by_id")
@patch("crud.security.jwt.decode")
def test_get_current_user_success(mock_decode, mock_get_user_by_id, db_session, mock_user):
    mock_decode.return_value = {"sub": "test_user_id"}
    mock_get_user_by_id.return_value = mock_user

    response = client.get(
        "/test-current-user",
        headers={"Authorization": "Bearer test_token"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "UserId": "test_user_id",
        "UserName": "test_user",
        "UserEmail": "test_user@example.com",
        "UserEmailVerified": True,
        "Is_Ban": False,
    }

# 测试令牌过期
@patch("crud.security.jwt.decode")
def test_get_current_user_expired_token(mock_decode, db_session):
    mock_decode.side_effect = jwt.ExpiredSignatureError

    response = client.get(
        "/test-current-user",
        headers={"Authorization": "Bearer expired_token"},
    )

    assert response.status_code == 401
    assert response.json() == {"detail": "Token has expired"}

# 测试无效令牌
@patch("crud.security.jwt.decode")
def test_get_current_user_invalid_token(mock_decode, db_session):
    mock_decode.side_effect = jwt.InvalidTokenError

    response = client.get(
        "/test-current-user",
        headers={"Authorization": "Bearer invalid_token"},
    )

    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid token"}

# 测试未认证用户
def test_get_current_user_no_token():
    response = client.get("/test-current-user")

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Not authenticated. Use either JWT token or API key.",
        "headers": {"WWW-Authenticate": "Bearer or ApiKey"},
    }