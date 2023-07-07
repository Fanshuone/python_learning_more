# coding:utf-8
from multiprocessing import Pool
import time
import os


# 编写任务
def task(name):
    print(f'子进程的PID：{os.getpid()},执行任务---task---{name}')
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print('父进程开始执行')
    # 创建一个进程池
    p = Pool(3)  # 进程池里，最大进程的个数

    # 创建10个进程
    for i in range(10):
        # 以非阻塞方式进行
        # p.apply_async(func=task,args=(i,))
        # 以阻塞方式进行
        p.apply(func=task, args=(i,))
    p.close()  # 关闭进程池，不再接收新任务
    p.join()  # 阻塞父进程，等待子进程结束
    print('所有子进程结束，父进程执行结束')
    print(time.time() - start)
