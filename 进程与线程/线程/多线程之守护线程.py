# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import threading

import time, os


class MyThread(threading.Thread):

    def run(self):
        for i in range(3):
            print("线程名字%s,输出:%d" % (self.name, i))  # 自定义的线程类，可以从父类中继承name属性
            time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print("主线程开始时间:%s" % start)

    # 创建一个线程
    t = MyThread(name='my_thread-1')  # 创建线程 ,里面参数代表线程的名字，如果不传，系统会默认有一个名字。
    t.daemon = True  # 当前子线程设置为守护线程
    # t.daemon =True #和上面的代码一样
    t.start()  # 启动线程

    # 等待所有的子线程都停止之后，主线程才中止
    time.sleep(1)
    end = time.time()
    print('主线程结束:中间执行的时间为%.2f' % (end - start))
