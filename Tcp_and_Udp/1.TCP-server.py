# coding:utf-8
import socket  # 导入

ip = '127.0.0.1'
port = 8888
print('--------------------服务器端已启动------------------------')
# （1）创建socket对象  socket.AF_INET用于Internet之间进程通信 ，socket.SOCK_STREAM用于TCP协议
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# (2)绑定主机和端品
socket_obj.bind((ip, 8888))

# (3)设置最大的连接数量
socket_obj.listen(5)
# (4)被动等待客户端TCP 连接
client_socket_obj, addr = socket_obj.accept()
print('-------------成功建立连接------------------')
# (5)接收客户端发送过来的数据
info = client_socket_obj.recv(1024).decode(encoding='utf-8')
while info != 'bye':
    if info != '':
        print('接收到的数据是:', info)
    # 准备发送信息
    data = input('请输入要发送的内容:')
    client_socket_obj.send(data.encode(encoding='utf-8'))
    if data == 'bye':
        break
    info = client_socket_obj.recv(1024).decode(encoding='utf-8')

# 关闭socket
client_socket_obj.close()
socket_obj.close()
