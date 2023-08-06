# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import threading

import time, os


class MyThread(threading.Thread):

    def __init__(self, name):
        # threading.Thread.__init__(self,name=name)

        super().__init__(name=name)

    def run(self):
        for i in range(3):
            print("线程名字%s,输出:%d" % (self.name, i))  # 自定义的线程类，可以从父类中继承name属性
            time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print("主线程开始时间:%s" % start)

    thread_list = []
    # 创建多个线程
    s = "abcdef"
    for i in range(5):
        t = MyThread(name=s[i])  # 创建线程 ,里面参数代表线程的名字，如果不传，系统会默认有一个名字。
        t.start()  # 启动线程
        thread_list.append(t)
    # 等待所有的子线程都停止之后，主线程才中止
    for j in thread_list:
        j.join()
    end = time.time()
    print('主线程结束:中间执行的时间为%.2f' % (end - start))
