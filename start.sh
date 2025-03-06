#!/bin/bash

# 激活虚拟环境
source ./venv/Scripts/activate

# 转到 Back_End 目录
cd Back_End

# 启动 Uvicorn 服务器
uvicorn main:app --reload