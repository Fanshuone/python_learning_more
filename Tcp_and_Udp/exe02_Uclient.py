from socket import *

# 创建套接字
socket_client = socket(AF_INET, SOCK_DGRAM)

# 2 定义一个接受消息的目标
SERVER_IP_PORT = ("192.168.0.101", 8090)


# 3 发送数据
datas = input("请输入：").encode(encoding="utf-8")

socket_client.sendto(datas,SERVER_IP_PORT)

print("发送完成")

# 关闭套接字

# socket_client.close()



