# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

# 信号量： 设置在多线程中，并行运行的线程个数

import threading
import time

semapshore = threading.BoundedSemaphore(3) #一次只运行同时三个人过安检

def run(num):
    semapshore.acquire()
    print('第{}个人正在过安检'.format(num))
    time.sleep(5)
    semapshore.release()

if __name__ == '__main__':
    for i in range(100):
        thread = threading.Thread(target=run,args=(i,))
        thread.start()