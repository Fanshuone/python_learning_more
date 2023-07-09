from socket import *
import struct  # 复杂的python数据结果和C语言的数据结构转换
file_name = input("请输入文件名字：")
# 客户端的socket
socket_client = socket(family=AF_INET, type=SOCK_DGRAM)

# 定义服务器的地址和端口号
host_port = ("192.168.0.101", 69)
# '!h%dsb5sb' 代表格式： ！开头
# 请求的数据包
data_package = struct.pack('!H%dsb5sb' %len(file_name),1,file_name.encode('utf-8'),0,'octet'.encode('utf-8'),0)

# 将数据包
socket_client.sendto(data_package,host_port)

# 客户端首先创建一个空白文件

f = open('client_' + file_name,'ab')

while 1:
    # 客户端接收数据，数据只有两种： 1 下载文件内容数据报 2 error 信息报
    recv_data, (server_ip, server_port) = socket_client.recvfrom(1024)
    operator_code, num = struct.unpack('!HH',recv_data[:4])
    if int(operator_code) == 5:
        print("服务器返回：你要下载的文件不存在")
        break

    # 如果是文件数据的数据包，则保存文件

    f.write(recv_data[4:])

    # 判断是否是最后一次传输
    if len(recv_data) < 516:
        print("客户端下载成功")
        break

    # 客户端收到数据包之后，还需要发送一个确认ACK给服务器

    ack_package = struct.pack('!HH',4,num)
    socket_client.sendto(ack_package,(server_ip, server_port))

f.close()
socket_client.close()