def fib_a(times):
    # 初始化
    n = 0
    a, b = 0, 1
    while n < times:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


f = fib_a(5)
print(f)
print(f.__next__())
print(f.__next__())
print(f.send('vsda'))
print(f.__next__())
print(f.__next__())
# print(f.__next__())
# print(f.__next__())


def fib_a(times):
    # 初始化
    n = 0
    a, b = 0, 1
    while n < times:
        yield (b)
        a, b = b, a + b
        n += 1
    return 'done'


for i in fib_a(5):
    print(i)


def fib_d(times):
    # 初始化
    n = 0
    a, b = 0, 1
    while n < times:
        yield (b)
        a, b = b, a + b
        n += 1
    return 'done'


f = fib_d(5)
while True:
    try:
        x = next(f)
        print("value:%d" % x)
    except StopIteration as e:
        print(e)
        print("⽣成器返回值:%s" % e.value)
        break
