from socket import *

# 创建一个服务端的socket

socker_server = socket(AF_INET, SOCK_DGRAM)

# 定义服务器端的地址和端口号

host_port = ("192.168.0.101", 8090)
# host_port = ("0.0.0.0", 8090)

# 服务器端的Socker来绑定地址和端口,只有绑定了地址和端口，才能称之为服务器的socket

socker_server.bind(host_port)

# 接收客户端的发送数据，每次接受1kb的数据  收到的数据报，里面的值是元组，第一个值是数据内容，第二个值是源地址和源端口号

data = socker_server.recvfrom(1024)
print(data)
print(data[0].decode(encoding="utf-8"))

# 关闭套接字，释放资源
socker_server.close()
