# coding:utf-8
"""
在操作系统中，每个进程都有一个唯一的进程标识符（PID），用于标识该进程。
在 Python 中，可以使用 os 模块的 getpid() 函数来获取当前进程的 PID。
"""
from multiprocessing import Process
# 定义函数，函数中的代码就是进程要执行的代码
import os
import time


def test():
    print(f'我是子进程，我的PID是:{os.getpid()}，我的父进程是:{os.getppid()}')
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()  # 开始时间
    lst = []
    print('主进程开始执行:')
    # 创建5个子进程
    for i in range(5):
        # 创建一个子进程对象
        pro = Process(target=test)
        # 启动进程
        pro.start()
        # 启动的进程添加到列表中
        lst.append(pro)
    # 列表中每个成员都是一个进程
    for item in lst:
        item.join()  # 阻塞主进程

    print(f'运行5个子进程一共花了:{time.time() - start}')
    print('主进程执行结束')  # 只是主进程中没有代码了，但并不是主进程结束
# 主进程要等到所有的子进程结束之后才会结束

