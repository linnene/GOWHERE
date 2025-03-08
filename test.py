import secrets

secret_key = secrets.token_hex(32)  # 生成一个 32 字节的十六进制字符串
print(secret_key)