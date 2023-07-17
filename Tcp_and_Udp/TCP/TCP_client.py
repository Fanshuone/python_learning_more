import time
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)

# 客户端发送链接的请求(仅仅创建链接)
server_ip_port = ("192.168.0.101", 8088)
client_socket.connect(server_ip_port)

send_data = input("请输入：")
client_socket.send(send_data.encode('utf-8'))

# 接受服务器返回的数据

recv_data = client_socket.recv(1024)

print("服务器发送的数据是：",recv_data.decode('utf-8'))
client_socket.close()
time.sleep(5)