import socket
hostname = socket.gethostname()
print(f"Original Hostname: {hostname}")

# 尝试转换为 ASCII
ascii_hostname = hostname.encode("idna").decode("ascii")
print(f"Converted Hostname: {ascii_hostname}")
