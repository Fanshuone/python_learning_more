# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

import threading
import time
import queue


#创建一个队列 ，1000代表maxSize
q = queue.Queue(1000) # 先进先出的队列
# q = queue.LifoQueue #后进先出
# q = queue.PriorityQueue # 优先级的队列

#定义生产者线程
class Producer(threading.Thread):

    def run(self):
        global  q
        count = 0
        while True:
            if q.qsize()<1000:
                #直接生成100条
                for i in range(100):
                    count +=1
                    msg = "产品{}".format(count)
                    q.put(msg)
                    print(msg)
            time.sleep(2)

#定义消费者线程
class Consumer(threading.Thread):
    def run(self):
        global q
        while True:
            for i in range(100):
                msg = q.get()
                print("消费线程得到了数据:{}".format(msg))
            time.sleep(3)

if __name__ == '__main__':
    t1 = Producer()

    t2 = Consumer()

    t1.start()
    t2.start()
