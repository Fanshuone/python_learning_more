# coding:utf-8
import socket

# 创建socket对象
client_socket = socket.socket()
# 主机服务器IP地址
ip = '127.0.0.1'
# 主机服务器程序的端口
port = 8888
# 连接服务器
client_socket.connect((ip, port))
print('--------已建立服务器连接----------------')
info = ''
while info != 'bye':
    send_data = input('请客户端输入要发送的数据:')
    client_socket.send(send_data.encode(encoding='utf-8'))
    if send_data == 'bye':
        break
    info = client_socket.recv(1024).decode(encoding='utf-8')
    print('收到服务器的响应数据是:', info)

client_socket.close()
