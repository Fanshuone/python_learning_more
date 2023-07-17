# -*- coding: utf-8 -*-
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(('192.168.5.180', 8008))

while True:
    send_data = input("send:")

    if len(send_data) > 0:
        client_socket.send(send_data.encode('utf-8'))
    if send_data == 'exit':
        client_socket.close()
        break

    # 客户端结束服务器返回的内容
    recv_data = client_socket.recv(1024)
    print("服务器:", recv_data.decode('utf-8'))

client_socket.close()
