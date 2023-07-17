"""
此代码旨在测试tcp client socket close的情况下，tcp server 将要 reve len(data) == 0 的数据
"""

import socket

# 创建客户端套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
server_address = ('localhost', 12345)
client_socket.connect(server_address)
print("已连接到服务器：", server_address)

# 发送数据到服务器
client_socket.sendall(b"Hello, server!")

# 关闭连接
client_socket.close()
