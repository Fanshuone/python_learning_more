# coding:utf-8
class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    a = A()  # 创建A类的对象
    b = B()  # 创建B类的对象
    c = C('陈梅梅', 20)  # 创建C类的对象
    print(a.__dict__)  # 对象的属性字典
    print(c.__dict__)
    print(a.__class__)  # 对象所属的类
    print(b.__class__)
    print(c.__class__)
    print(A.__bases__)  # 类的父类，结果是一个元组
    print(C.__bases__)
    print(A.__base__)  # 类的父类，如果是继承多个父类，结果是第一个父类
    print(C.__base__)
    print(A.__mro__)  # A 类继承了object类
    print(C.__mro__)  # C类继承了A，和B类，A,B 这两个类又继承了object

    # 用于获取类的子类列表
    print(A.__subclasses__())  # A的子类有C
    print(C.__subclasses__())  # C没有子类,空列表
