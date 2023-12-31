# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

from multiprocessing import Process, Pipe
import os, time


# 创建两个进程，一个进程负责读，一个负责写

# 负责写的进程,
class WriterProcess(Process):

    def __init__(self, xname, pipe):
        Process.__init__(self)
        self.name = xname
        self.pipe = pipe

    def run(self):
        # 把多条数据写入到队列中
        print("进程名字:%s,ID:%s;已经启动" % (self.name, os.getpid()))
        for i in range(1, 6):
            self.pipe.send(i)  # writer进程负责把数据通过管道发送给另外一个进程
            time.sleep(1)  # 休眠一秒
        print("进程名字:%s,ID:%s;已经结束" % (self.name, os.getpid()))


# 负责读取队列中的数据
class ReaderProcess(Process):

    def __init__(self, xname, pipe):
        Process.__init__(self)
        self.name = xname
        self.pipe = pipe

    def run(self):
        print("进程名字:%s,ID:%s;已经启动" % (self.name, os.getpid()))
        while True:
            # recv函数是一个阻塞的函数
            value = self.pipe.recv()  # 当管道中没有数据，该行代码一直阻塞者
            print(value)
        # 不会执行的代码
        print("进程名字:%s,ID:%s;已经结束" % (self.name, os.getpid()))


if __name__ == '__main__':
    p1, p2 = Pipe()  # Pipe创建之后得到管道的两端
    pw = WriterProcess('writer', p1)
    pr = ReaderProcess('reader', p2)

    # 启动两个进程
    pw.start()
    pr.start()

    # 让父进程等待子进程结束
    pw.join()
    # pr进程是一个死循环
    pr.terminate()  # 强制杀死pr进程
    print("父进程结束")
