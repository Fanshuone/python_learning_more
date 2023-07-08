import socket

client_socker = socket.socket()

ip = '127.0.0.1'
port = 9876

client_socker.connect((ip,port))
info = ''
while info != 'bye':
    send_data = input('请客户端输入要发送的数据 ')
    client_socker.send(send_data.encode(encoding='utf-8'))
    if send_data == 'bye':
        break
    info = client_socker.recv(1024).decode(encoding='utf-8')
    print('服务器响应数据是：',info)

