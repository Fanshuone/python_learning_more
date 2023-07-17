import socket

# 创建服务器套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器地址和端口
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# 监听连接
server_socket.listen(1)
print("等待客户端连接...")

# 接受客户端连接
client_socket, client_address = server_socket.accept()
print("客户端已连接：", client_address)

# 接收客户端发送的数据
while True:
    data = client_socket.recv(1024)
    if not data:  # 客户端关闭了连接
        print("客户端已下线")
        break
    print("收到客户端数据：", data.decode())

# 关闭连接
client_socket.close()
server_socket.close()
