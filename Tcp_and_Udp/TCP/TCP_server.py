from socket import *

# 1 创建server_socket

server_socket = socket(AF_INET, SOCK_STREAM)

# 2 绑定一个IP 和 端口

host_port = ("", 8088)

server_socket.bind(host_port)

# 3 服务器的socket监听,listen让socket处于监听状态,允许多个客户端链接请求排队

server_socket.listen(5)
while 1:
    # 4 等待客户端的链接请求,当前函数处于阻塞状态
    #   返回两个返回值： 1 新的socket 2
    new_socket, client_addr = server_socket.accept()

    # 5 服务器接受客户端发送过来的数据, recv一般用于tcp协议接收数据，recvfrom一般用于udp数据
    data = new_socket.recv(1024)

    print("服务器接受的数据是： ", end="")
    print(data.decode(encoding='utf-8'))

    # 6 向客户端发送消息
    new_socket.send("Thank you ".encode(encoding='utf-8'))

    # new_socket 关闭 意味着关闭与当前客户端的链接
    new_socket.close()
# 整个服务器关闭
server_socket.close()


