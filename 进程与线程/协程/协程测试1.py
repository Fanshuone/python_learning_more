# -*- coding: utf-8 -*-
# 教育机构：马士兵教育
# 讲师： 肖 斌

import gevent


# 开发协程的案例，一个任务是回答，一个任务是问

def ask(name):
    print("%s : 我要买个手提包！" % name)  # 2
    f = open("a.txt",'w')
    for i in range(10000000):
        f.write("fffff")
    f.close()
    a=0
    for i in range(10000):
        a+=1
    print("a: ",a)
    # gevent.sleep(0)  # 人为的模拟IO阻塞
    print("%s : 我想要学个Python！" % name)  # 4


def answer(name):
    print("%s : 买买买！！" % name)  # 3

    # gevent.sleep(0)
    b = 0
    for i in range(10000):
        b += 1
    print("b: ", b)
    print("%s :可以买，一定去马士兵教育!" % name)


if __name__ == '__main__':
    import time

    start = time.process_time()
    a = gevent.spawn(ask, '小乔')  # 创建一个协程
    b = gevent.spawn(answer, '周瑜')  # 创建第二个协程
    gevent.joinall([a, b])  # 自动切换并行执行
    end = time.process_time()

    print("消耗时间", start - end)


