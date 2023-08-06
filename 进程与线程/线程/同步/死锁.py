# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

import threading

import  time

# 代表鱼的锁
mutex_Yu = threading.Lock()

# 代表熊掌的锁
mutex_XiongZhang = threading.Lock()

class MyThread1(threading.Thread):
    def run(self):
        mutex_Yu.acquire() # 得到鱼
        print("线程1已经得到鱼了")
        time.sleep(1)

        mutex_XiongZhang.acquire()
        print("线程1得到熊掌")
        mutex_XiongZhang.release()
        mutex_Yu.release()

class MyThread2(threading.Thread):
    def run(self):
        mutex_XiongZhang.acquire()
        print("线程2已经得到熊掌了")
        time.sleep(1)
        mutex_Yu.acquire()  # 得到鱼
        print("线程2已经得到鱼了")
        mutex_Yu.release()
        mutex_XiongZhang.release()




# 第二种死锁情况

# mutex_TianTang = threading.Lock() #去天堂的锁 ,Lock()  其实是互斥锁。可以使用逻辑锁，这样就不会死锁了

mutex_TianTang = threading.RLock() # Rlock就是逻辑锁,但是针对一个线程才可以使用逻辑锁

class MyThread3(threading.Thread):
    def run(self):
        mutex_TianTang.acquire()
        print("线程3进入了天堂")
        time.sleep(1)
        self.run() #再次进入天堂

        mutex_TianTang.release()


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()

    # t3 = MyThread3()
    # t3.start()