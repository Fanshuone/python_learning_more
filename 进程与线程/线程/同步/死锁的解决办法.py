# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

#让多个线程交叉有序的竞争多个资源
import threading

import  time

# 代表鱼的锁
mutex_Yu = threading.Lock()

# 代表熊掌的锁
mutex_XiongZhang = threading.Lock()

class MyThread1(threading.Thread):
    def run(self):

        while True:
            mutex_Yu.acquire() # 得到鱼
            print("线程1已经得到鱼了")
            time.sleep(1)
            mutex_Yu.release() #释放鱼对应锁


            mutex_XiongZhang.acquire()
            print("线程1得到熊掌")
            time.sleep(1)
            mutex_XiongZhang.release()

class MyThread2(threading.Thread):
    def run(self):
        while True:
            mutex_XiongZhang.acquire()
            print("线程2已经得到熊掌了")
            time.sleep(1)
            mutex_XiongZhang.release()

            mutex_Yu.acquire()  # 得到鱼
            print("线程2已经得到鱼了")
            time.sleep(1)
            mutex_Yu.release()





if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
