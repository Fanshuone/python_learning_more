# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

from multiprocessing import Process, Queue
import os, time

# 创建两个进程，一个进程负责读，一个负责写
num = 100  # 多个进程之间是不能共享父进程的全局变量。


# 负责写的进程,
class WriterProcess(Process):

    def __init__(self, xname, mq):
        Process.__init__(self)
        self.name = xname
        self.mq = mq

    def run(self):
        global num
        num = 200
        print(num)
        # 把多条数据写入到队列中
        print("进程名字:%s,ID:%s;已经启动" % (self.name, os.getpid()))
        for i in range(1, 6):
            self.mq.put(i)  # writer进程负责把数据写入Queue
            time.sleep(1)  # 休眠一秒
        print("进程名字:%s,ID:%s;已经结束" % (self.name, os.getpid()))


# 负责读取队列中的数据
class ReaderProcess(Process):

    def __init__(self, xname, mq):
        Process.__init__(self)
        self.name = xname
        self.mq = mq

    def run(self):
        print("进程名字:%s,ID:%s;已经启动" % (self.name, os.getpid()))
        while True:
            # get函数是一个阻塞的函数
            value = self.mq.get(True)  # 当队列中没有数据，该行代码一直阻塞者
            print(value)
        # 不会执行的代码
        print("进程名字:%s,ID:%s;已经结束" % (self.name, os.getpid()))


if __name__ == '__main__':
    q = Queue()
    pw = WriterProcess('writer', q)
    pr = ReaderProcess('reader', q)

    # 启动两个进程
    pw.start()
    pr.start()

    # 让父进程等待子进程结束
    pw.join()
    # pr进程是一个死循环
    pr.terminate()  # 强制杀死pr进程
    print("父进程结束")
    print(num)
