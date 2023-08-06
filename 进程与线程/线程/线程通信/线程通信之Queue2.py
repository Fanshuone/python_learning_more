# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

import threading
import time
import queue

#创建一个队列 ，1代表maxSize
q = queue.Queue(1) # 先进先出的队列
# q = queue.LifoQueue #后进先出
# q = queue.PriorityQueue # 优先级的队列

#定义生产者线程
class Producer(threading.Thread):

    def run(self):
        global  q
        count = 0
        while True:
            time.sleep(1)
            print("生产线程开始生成数据")
            count +=1
            msg = "产品{}".format(count)
            q.put(msg)
            print(msg)

#定义消费者线程
class Consumer(threading.Thread):
    def run(self):
        global q
        while True:
            print('消费线程已经开始消费了')
            msg = q.get() # 默认阻塞
            print("消费线程得到了数据:{}".format(msg))
            time.sleep(5)

if __name__ == '__main__':
    t1 = Producer()

    t2 = Consumer()
    t3 = Consumer()

    t1.start()
    t2.start()
    t3.start()
