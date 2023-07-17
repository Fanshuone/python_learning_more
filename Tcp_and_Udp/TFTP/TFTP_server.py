import struct
from socket import *

socker_server = socket(AF_INET, SOCK_DGRAM)

socker_server.bind(('', 69))


def download(file, client_ip, client_port):
    # 创建一个新的Socket 负责发送文件内容的数据包到客户端
    new_socket = socket(AF_INET, SOCK_DGRAM)
    # 文件内容数据包的计数器
    num = 1
    flag = True
    f = None
    try:
        f = open(file, 'rb')

    except:

        error_package = struct.pack('!HH5sb', 5, 5, 'error'.encode('utf-8'), 0)
        # 把错误数据发出给客户端
        new_socket.sendto(error_package, (client_ip, client_port))
        new_socket.close()
        flag = False

    # 如果文件存在， 那么需要把文件的内容切成一个个数据包发送给客户端，一个数据包包含内容为512字节

    while flag:
        # 从文件内容中读取512字节数据
        # if num == 150:
        #     read_data = f.read(512)
        #     num += 1
        #     continue
        read_data = f.read(512)
        data_package = struct.pack('!HH', 3, num) + read_data
        # 发送数据包
        new_socket.sendto(data_package, (client_ip, client_port))

        # 文件内容的数据即将下载完
        if len(read_data) < 512:
            print("客户端：%s 文件下载完成" % client_ip)
            # 当前客户端退出
            break

        # 服务器接受ACK的确认数据
        recv_ack = new_socket.recvfrom(1024)
        operator_code, ack_number = struct.unpack("!HH", recv_ack[0])
        print("客户端： %s,确认的信息是 %s" % (client_ip, ack_number))
        num += 1

        # 保护性代码
        # 不正常的ack确认信息
        if int(operator_code) != 4 or int(ack_number) < 1:
            break
    if f:
        f.close()
    new_socket.close()


def server():
    while True:
        # 服务器等着客户端发送数据，并接收
        recv_data, (client_ip, client_port) = socker_server.recvfrom(1024)
        # print(recv_data, client_ip, client_port)
        # unpack_data = struct.unpack('!H4sb5sb', recv_data)
        # print(unpack_data)

        unpack_data = struct.unpack('!b5sb', recv_data[-7:])
        # print(unpack_data)
        # 判断数据包是否是：客户端请求数据包
        if unpack_data == (0, b'octet', 0):
            # 得到操作码的值
            operate_code = struct.unpack("!H", recv_data[:2])
            # 得到文件名字
            file_name = recv_data[2:-7].decode(encoding='utf-8')
            print(operate_code, file_name)
            # 如果等于1， 就是下载的请求数据包
            if operate_code[0] == 1:
                print("客户端想下载文件: %s " % file_name)
                download(file_name, client_ip, client_port)


server()
