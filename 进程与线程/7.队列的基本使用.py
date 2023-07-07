# coding:utf-8
from multiprocessing import Queue

if __name__ == '__main__':
    # 创建一个队列，最多可以接收3条消息
    q = Queue(3)
    print('队列是否为空:', q.empty())
    print('队列是否为满:', q.full())
    # 向队列中添加消息
    q.put('hello')  # block默认为True
    q.put('world')
    print('队列是否为空:', q.empty())
    print('队列是否为满:', q.full())
    q.put('python')
    print('队列是否为空:', q.empty())
    print('队列是否为满:', q.full())
    print('队列中消息的个数：', q.qsize())
    # 队列中已满，还能否添加数据呢？
    # q.put('html') #队列已满,block=True默认为True，一直等待队列有空位置才会 将html入队，然后继续执行
    # q.put('html',block=True,timeout=2) #等待2秒，还没有空位置，抛出异常queue.Full
    # q.put_nowait('html') # 相当于q.put('html',block=False) #queue.Full
    print('------------------')
    # 从列表中获取消息，出队的操作
    print(q.get())
    print('出队之后，消息的个数:', q.qsize())
    q.put_nowait('html')  # 入队
    print('入队之后，消息的个数', q.qsize())
    # 通过遍历出队所有元素
    if not q.empty():  # 判断队列是否为空
        for i in range(q.qsize()):
            print(q.get_nowait())

    print('队列是否为空:', q.empty())
    print('队列是否为满:', q.full())
    print('队列中消息的个数：', q.qsize())
