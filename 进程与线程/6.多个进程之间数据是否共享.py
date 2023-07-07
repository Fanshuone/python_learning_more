# coding:utf-8
"""global 是 Python 中的关键字，用于在函数内部引用全局变量或在函数内部修改全局变量的值。它的作用有以下几个方面：

在函数内部引用全局变量：当函数内部需要引用全局作用域中的变量时，可以使用 global 关键字将该变量声明为全局变量。
这样，在函数内部就可以访问和使用该全局变量了。

在函数内部修改全局变量的值：在 Python 中，默认情况下，函数内部无法直接修改全局变量的值，而只能创建一个同名的局部变量。
但是，如果在函数内部使用 global 关键字声明了一个变量，那么在函数内部对该变量的赋值操作就会修改全局作用域中的变量。"""

from multiprocessing import Process

a = 100


def fun(num):
    print('fun',num)


def add():
    print('子进程1开始执行')
    global a
    a += 30
    print('a=', a)
    fun(a)
    print('子进程1执行结束')


def sub():
    print('子进程2开始执行')
    global a
    a -= 50
    print('a=', a)
    fun(a)
    print('子进程2执行结束')


if __name__ == '__main__':
    print('父进程开始执行')
    print('a的值为:', a)
    # 创建加的进程
    p1 = Process(target=add)
    # 创建减的进程
    p2 = Process(target=sub)
    # 启动两个子进程
    p1.start()
    p2.start()
    # 等待p1进程执行结束
    p1.join()
    # 等待p2进程执行结束
    p2.join()

    print('父进程执行结束')
