# coding:utf-8
from threading import Thread

a = 100


def add():
    print('加的线程开始执行')
    global a
    a += 30
    print(f'a的值为:{a}')
    print('加的线程执行结束')


def sub():
    print('减的线程开始执行')
    global a
    a -= 50
    print(f'a的值为:{a}')
    print('减的线程执行结束')


if __name__ == '__main__':
    print('主线程开始执行')
    print(f'------全局变量a的值{a}-------')
    add = Thread(target=add)
    sub = Thread(target=sub)
    # 启动线程
    add.start()
    sub.start()
    add.join()  # 等待加的线程结束
    sub.join()  # 等待减的线结束
    print('--------主线程执行结束-----')
