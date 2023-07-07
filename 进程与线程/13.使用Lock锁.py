# coding:utf-8
# coding:utf-8
import threading
from threading import Thread, Lock
import time

ticket = 50
lock_obj = Lock()  # 创建锁对象


def sale_ticket():
    global ticket
    for i in range(1000):
        lock_obj.acquire()  # 加锁
        if ticket > 0:
            print(threading.current_thread().name + f'正在出售第{ticket}张票')
            ticket -= 1
        time.sleep(1)
        lock_obj.release()  # 释放锁


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=sale_ticket)
        t.start()
