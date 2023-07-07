# coding:utf-8
from multiprocessing import Process, Queue
import time

a = 100


# 向队列中写入消息的进程要执行的函数
def write_msg(q):
    global a
    if not q.full():
        for i in range(1, 6):
            a -= 10
            q.put(a)  # 入队操作，将a的值进行入队
            print('a入队时的值:', a)


# 从队列中读取消息的进程要执行的函数
def read_msg(q):
    time.sleep(1)
    while not q.empty():
        print('出队a的值:', q.get())


if __name__ == '__main__':
    print('父进程开始执行')
    q = Queue()  # 由父进程创建队列，传给子进程,没有写个数，说明队列可接收的消息个数没有上限
    # 创建两个子进程
    p1 = Process(target=write_msg, args=(q,))
    p2 = Process(target=read_msg, args=(q,))
    # 启动两个子进程
    p1.start()
    p2.start()
    # 等待写入进程结束
    p1.join()
    # 等待读取进程结束
    p2.join()

    print('----------------------父进程执行结束---------------')
