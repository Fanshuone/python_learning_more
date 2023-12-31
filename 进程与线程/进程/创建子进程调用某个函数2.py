# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
# 封装一个进程类

from multiprocessing import Process
import os
import time

a = 100


# 自定义一个进程类
class MyProcess(Process):

    def __init__(self, xname):
        Process.__init__(self)  # 加载父类给我们提供的功能
        self.name = xname

    def run(self):  # 子进程在运行过程中执行的代码
        print('当前进程的ID', os.getpid())  # getpid获取当前调用函数的进程id
        print("父进程的ID", os.getppid())  # getppid获取当前进程的父进程ID
        print('当前进程的名字', self.name)
        a = 200
        print('子进程里面打印a', a)
        time.sleep(3)


if __name__ == '__main__':

    # 当前开始的时间戳
    start = time.time()
    # 创建10个子进程放入一个列表中
    process_list = []
    for i in range(10):
        p = MyProcess('process-%d' % (i + 1))  # 创建我们自定义的进程类
        p.start()
        process_list.append(p)

    for p in process_list:
        # 我们一般都会需要父进程等待所有子进程结束，才执行后面的代码,join等待当前的子进程p结束
        p.join()  # 10个子进程可以并行执行

    # 所有子进程已经结束了
    r = time.time() - start
    print('十个子进程一共执行的时间是', r)
    print("父进程最后打印a", a)
