# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

#粘包问题2 ：接收方的粘包问题

import socket
import time

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('',9999))

server_socket.listen(5)

new_socket,client_addr = server_socket.accept()

print('连接成功',client_addr)

data1 = new_socket.recv(3) #第一次没有接受完整
print("第一个数据包",data1)
time.sleep(6)
data2 = new_socket.recv(10) # 第二次会接受旧数据，然后如果还有空间再接受新数据
print("第二个数据包",data2)


new_socket.close()
server_socket.close()
