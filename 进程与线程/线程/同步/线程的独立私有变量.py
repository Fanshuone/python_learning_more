# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
from threading import *
import time, random


# 让每个线程拥有一个独立的，私有变量。
# local_var = local()
def run():
    # 创建一个独立的，私有变量
    local_var = local()
    local_var.numbers = [1]  # 每个线程先给一个初始值1
    # 为了模拟线程执行的时间不同
    time.sleep(random.random())  # 随机休眠时间
    for j in range(8):
        # 在私有变量中放入随机的数字
        local_var.numbers.append(random.choice(range(10)))
    # 打印当前线程的私有变量值
    print(current_thread(), local_var.numbers)


if __name__ == '__main__':
    threads = []  # 线程的列表,方便调用join

    for i in range(5):
        t = Thread(target=run)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
