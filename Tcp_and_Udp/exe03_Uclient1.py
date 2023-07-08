from socket import *

# 创建套接字
socket_client = socket(AF_INET, SOCK_DGRAM)

# 2 定义一个接受消息的目标
SERVER_IP_PORT = ("192.168.0.101", 8090)

flag = True
#  定义变量，是否退出客户端的标志
while flag:
    # 3 发送数据
    datas = input("请输入：").encode(encoding="utf-8")

    socket_client.sendto(datas,SERVER_IP_PORT)

    print("发送完成")

    data_recv = socket_client.recvfrom(1024)[0].decode(encoding='utf-8')  # ctrl alt v 变量声明
    print("返回的数据是：", data_recv)
    if data_recv == 'exit':
        flag = False
    # 关闭套接字

socket_client.close()



