# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

from socket import *
import struct
import os

client = socket(AF_INET, SOCK_STREAM)
client.connect(('192.168.5.180', 8088))

# 客户端传送一个文件到服务器，进程.mp4
file_path = '进程.mp4'
f = open(file_path, 'rb')

# 在发送真正的文件数据之前，先准备一个报头
size = os.path.getsize(file_path)  # 文件的字节长度
# 创建一个报头，i为4个字节的int。
header = struct.pack('!i', size)  # 接收方会使用struct解包，得到一个int类型数字
client.send(header)

# 发送文件内容
while True:
    data = f.read(1024)  # 每次读取1024字节
    if not data:
        break
    client.send(data)  # 发送给服务器的文件内容

print("客户端上传文件完成")
f.close()
client.close()
