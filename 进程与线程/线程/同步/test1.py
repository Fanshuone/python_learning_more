import random
from threading import Thread

a = 0


def run():
    global a
    for i in range(500000):
        a += 1

    print(a)


if __name__ == '__main__':
    list1 = []
    for i in range(5):
        t = Thread(target=run)
        t.start()
        list1.append(t)

    for t in list1:
        t.join()
