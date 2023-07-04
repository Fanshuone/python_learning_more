"""
在单个子类继承两个父类，并且这两个父类都有一个同名的方法时，使用 super().方法() 调用父类方法时，首先会调用排在继承列表前面的父类的方法。

具体来说，调用 super().方法() 时，Python 会按照 MRO（Method Resolution Order，方法解析顺序）的规则，

从子类开始沿着继承链向上查找父类，找到第一个具有该方法的父类，并调用该父类的方法。

下面是一个示例代码，展示了在单个子类继承两个父类时，通过 super().方法() 调用父类方法的情况：
"""


class Parent1:
    def method(self):
        print("Parent1 method")


class Parent2:
    def method(self):
        print("Parent2 method")


class Child(Parent1, Parent2):
    def method(self):
        super().method()  # 调用继承列表中排在前面的父类 Parent1 的 method 方法


child = Child()
child.method()  # 输出: Parent1 method

"""
如果你想在子类中同时调用两个父类的同名方法，可以使用以下两种方法：
"""


class Parent1:
    def method(self):
        print("Parent1 method")


class Parent2:
    def method(self):
        print("Parent2 method")


class Child(Parent1, Parent2):
    def method(self):
        Parent1.method(self)  # 调用 Parent1 的 method 方法
        Parent2.method(self)  # 调用 Parent2 的 method 方法


child = Child()
child.method()  # 输出: Parent1 method
#      Parent2 method
