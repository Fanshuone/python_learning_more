# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

from socket import *

client_socket = socket(AF_INET,SOCK_STREAM)

client_socket.connect(('192.168.5.180',8080))

client_socket.send('hello'.encode('utf-8'))
client_socket.send('laoxiao'.encode('utf-8'))

client_socket.close()