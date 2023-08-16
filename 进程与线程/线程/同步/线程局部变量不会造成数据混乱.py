# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

from threading import *
import time



def run():
    print("当前进程%s,开始启动"%(current_thread().name))
    g_num =0
    for i in range(5000000):
        g_num +=1
    print('线程%s,执行之后g_num的值为:%s'%(current_thread().name,g_num))


if __name__ == '__main__':
    threads = []

    for i in range(5):
        t = Thread(target=run)
        t.start()
        threads.append(t)

    for j in threads:
        j.join()

    print('主线程结束')