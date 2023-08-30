def decor_a(fun):
    def decor_b():
        print('I am decor_b')
        fun()
        print('I am fun')

    return decor_b


@decor_a
def decor_c():
    print('I am decor_c')


def fun():
    print("测试函数名")


decor_c()

print(decor_c.__name__)
print(fun.__name__)


def log(func):
    def write_log(*args,**kwargs):
        print("开始写入")
        func(*args,**kwargs)
        print("写入完成")

    return write_log


@log
def work1():
    print("开始第一次写入")


@log
def work2(*args,**kwargs):
    print("开始第一次写入%d%d", args[0], args[1])


work1()
work2(1,2)