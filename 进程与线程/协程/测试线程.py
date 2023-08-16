from threading import Thread


def ask(name):
    print("%s : 我要买个手提包！" % name)  # 2
    a = 0
    for i in range(100000000):
        a += 1
    print("a: ", a)
    # gevent.sleep(0)  # 人为的模拟IO阻塞
    print("%s : 我想要学个Python！" % name)  # 4


def answer(name):
    print("%s : 买买买！！" % name)  # 3
    # gevent.sleep(0)
    b = 0
    for i in range(100000000):
        b += 1
    print("a: ", b)
    print("%s :可以买，一定去马士兵教育!" % name)


if __name__ == '__main__':
    import time
    start = time.process_time()
    t1 = Thread(target=ask,args=("貂蝉",))
    t2 = Thread(target=answer,args=("貂蝉",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end= time.process_time()

    print("消耗时间",start-end)