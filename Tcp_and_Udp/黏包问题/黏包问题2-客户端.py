# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

# 接收方可能出现的粘包问题

from socket import *
import time  # time模板保证客户端发送多个数据包的时候，间隔时间长

client = socket(AF_INET, SOCK_STREAM)

client.connect(('192.168.5.180', 9999))

client.send('mashibin'.encode('utf-8'))
time.sleep(5)  # 让当前的线程休眠5秒

client.send('laoxiao'.encode('utf-8'))

client.close()
