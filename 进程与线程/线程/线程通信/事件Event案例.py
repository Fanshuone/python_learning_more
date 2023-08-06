# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

import threading
import time
import random


#线程1，门，一开始是打开的，每3秒需要自动关闭一下。如果有人通过，需要重新刷卡打开
#线程2，人，人通过门，如果门是打开的直接通过，如果没有打开需要刷卡。之后门就已经大开了，通知人继续进入

event = threading.Event() #创建一个事件
event.set() # 设置标志位真 ，门一开始就是打开的

status = 0 # status代表门的状态，如果是0~3代表打开，如果等于3，需要关闭

def door():
    global status
    while True:
        print("当前门的status为:{}".format(status))
        if status>=3:
            print("当门已经打开了3秒，需要自动关闭")
            event.clear()
        if event.is_set():
            print('当前门是开着的，可以通行！')
        else:
            print('门已经关了，请用户自己刷卡!')
            event.wait() # 门的线程阻塞等待
            continue
        time.sleep(1)
        status+=1 # status代表们开始的秒数

def person():
    global status
    n =0 # 人的计数器，看看有多少人进入到门里面
    while True:
        n+=1
        if event.is_set():
            print('门开着，{}号人进入门里面'.format(n))
        else:
            print('门关着，{}号人刷卡之后，进入门里面'.format(n))
            event.set() # 标志改为true
            status =0
        time.sleep(random.randint(1,10))

if __name__ == '__main__':
    d = threading.Thread(target=door)
    p = threading.Thread(target=person)
    d.start()
    p.start()
