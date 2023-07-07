# coding:utf-8
# 继承方式创建线程
import threading
from threading import Thread
import time


class SubThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(f'线程{threading.current_thread().name}正在执行,i的值为{i}')


if __name__ == '__main__':
    print('主线程开始执行')
    lst = [SubThread() for i in range(2)]  # 创建2个线程，放到列表中存储
    for item in lst:
        item.start()  # 启动线程
    for item in lst:
        item.join()
    print('主线程执行结束')
