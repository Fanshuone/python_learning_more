# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('',8080))

server_socket.listen(5)

new_socket,client_addr = server_socket.accept()

data1 = new_socket.recv(1024)

data2 = new_socket.recv(1024)

print("第一条数据：",data1)
print("第二条数据：",data2)

new_socket.close()
server_socket.close()