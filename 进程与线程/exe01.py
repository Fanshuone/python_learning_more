import multiprocessing
import os
import time
from multiprocessing import Process


def fun():
    print(f"子进程pid-{os.getpid()}, 父进程pid-{os.getppid()}")


def fun2(num):
    print(f"{num}号子进程开始")
    time.sleep((1))


if __name__ == '__main__':
    # fun()
    #
    # f = Process(target=fun)
    # f.start()
    # f.join()
    # print("主进程结束")
    """
    注意这两种的区别
    """
    for i in range(5):
        f = Process(target=fun2, args=(i,))
        f.start()

        f.join()

    print("-------------------------------")
    lis = []
    for i in range(5):
        f = Process(target=fun2, args=(i,))
        print(f.is_alive())
        f.start()
        # time.sleep(1.5) 子进程结束 is_alive 为false
        print(f.is_alive())
        lis.append(f)

    for i in range(5):
        lis[i].join()

    print("主进程结束")
