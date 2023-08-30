def odd_unm():
    n = 1
    while 1:
        n += 2
        yield n


g = odd_unm()


# print(g.__next__())
# print(g.__next__())

def my_filter(n):
    return lambda x: x % n > 0


def tt():
    yield 2
    g = odd_unm()
    while 1:
        x = next(g)
        # print(list(g))
        g = filter(my_filter(x), g)
        print(next(g))
        print(next(g))
        print()
        yield x


for n in tt():
    if n < 1000:
        print("----",n)
        pass
    else:
        break

import numpy