# coding:utf-8
import threading
from threading import Thread
import time

ticket = 50


def sale_ticket():
    global ticket
    for i in range(1000):
        if ticket > 0:
            print(threading.current_thread().name + f'正在出售第{ticket}张票')
            ticket -= 1
        time.sleep(1)


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=sale_ticket)
        t.start()
