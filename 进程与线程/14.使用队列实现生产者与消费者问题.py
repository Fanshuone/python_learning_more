# coding:utf-8
from queue import Queue  # 实现线程之间的通信
# from multiprocessing import Queue
from threading import Thread
import time


# 创建一个生产者类
class Producer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 6):
            print(f'{self.name}将产品{i}放入队列')
            self.queue.put(i)
            time.sleep(1)
        print('生产者完成了所有数据的存放')


# 创建一个消费者类
class Consumer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for _ in range(5):
            value = self.queue.get()
            print(f'消费者线程{self.name}取出了{value}')
            time.sleep(1)
        print('--------------消费者线程完成了所有数据的取出------------------')


if __name__ == '__main__':
    # 创建队列
    queue = Queue()
    # 创建生产者线程
    p = Producer('Produce', queue)
    # 创建消费者线程
    con = Consumer('Consumer', queue)
    # 启动线程
    p.start()
    con.start()
    # 等待生产者线程结束，等待消费者线程结束
    p.join()
    con.join()
    print('主线程运行结束')
