import socket

ip = '127.0.0.1'
port = 9876

socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_obj.bind((ip,port))

socket_obj.listen(5)

client_socket_pbj , addr = socket_obj.accept()


info = client_socket_pbj.recv(1024).decode(encoding='utf-8')

while info != 'bye':
    if info != '':
        print('接收到的数据是：',info)

    data = input("请输入要发送的内容： ")
    client_socket_pbj.send(data.encode(encoding='utf-8'))
    if data == 'bye':
        break
    info = client_socket_pbj.recv(1024).decode(encoding='utf-8')

client_socket_pbj.close()
socket_obj.close()