def fun():
    return lambda :print("打印")


fun()()

class C():
    def __new__(cls, *args, **kwargs):
        pass

print(type(C))