"""
子类不重写__init__ ， 实例化子类时，会自动调用父类定义的__init__
但重写了__init__时，实例化子类，就不会调用父类已经定义的__init__
"""


class Parent:
    def __init__(self):
        self._private_attribute = 42

    def _private_method(self):
        print("This is a private method.")


class Child(Parent):
    def access_private_attribute(self):
        print(self._private_attribute)

    def call_private_method(self):
        self._private_method()


child = Child()
child.access_private_attribute()  # 输出: 42
child.call_private_method()  # 输出: This is a private method.


class Parent:
    def __init__(self):
        self._private_attribute = 42

    def _private_method(self):
        print("This is a private method.")


class Child(Parent):
    def __init__(self):
        super().__init__()  # 调用父类的 __init__() 方法来初始化属性

    def access_private_attribute(self):
        print(self._private_attribute)

    def call_private_method(self):
        self._private_method()


child = Child()
child.access_private_attribute()  # 输出: 42
child.call_private_method()  # 输出: This is a private method.
