# coding:utf-8
# 使用Process子类创建进程
from multiprocessing import Process
import os
import time


# 自定义类
class SubProcess(Process):
    # 初始化的方法
    def __init__(self, name):
        # 调用父类Process的初始化方法
        Process.__init__(self)
        self.name = name

    # 重写run方法
    def run(self):
        print(f'子进程的名称:{self.name}，PID:{os.getpid()},父进程的PID:{os.getppid()}')


if __name__ == '__main__':
    print('父进程开始执行')
    lst = []
    for i in range(1, 6):
        p1 = SubProcess(f'进程--{i}')
        # 启动进程
        p1.start()
        lst.append(p1)
    for item in lst:
        item.join()
    print('父进程执行结束')
