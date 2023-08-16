import time

a = 10


class C:
    def __init__(self):
        self.a = None

    def fun(self):
        self.a = 0


def f():
    c.fun()
    print(c.a)


# with open("xxx.tetx") as x:
class A():
    def fun(self):
        time.sleep(1)
        print("hahaha")
        self.fun()

class B:
    def __init__(self,path):
        self.path = path

    def __enter__(self):
        return  self

    def read(self):
        print("正在读取")

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

if __name__ == '__main__':
    a = 100
    b = 110
    c = C()
    f()
    print(a)
    a = A()
    print(a)
    print(A)

    with B("fanshu") as b:
        b.read()
    b.read()

    a=A()
    a.fun()