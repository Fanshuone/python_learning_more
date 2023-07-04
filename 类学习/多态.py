# coding:utf-8
"""
在面向对象编程中，多态是指使用相同的接口来处理不同类型的对象
"""


# 以下三个类都有一个同名的方法 eat()
class Person():
    def eat(self):
        print('人，吃五谷杂粮')


class Cat():
    def eat(self):
        print('猫，喜欢吃鱼')


class Dog():
    def eat(self):
        print('狗，喜欢啃骨头')


def fun(obj):  # 函数的定义处,obj是函数的形式参数
    obj.eat()  # 对象名打点调用eat方法


if __name__ == '__main__':
    per = Person()  # 创建Person类型的对象per
    cat = Cat()  # 创建Cat类的对象cat
    dog = Dog()  # 创建Dog类的对象dog

    # 调用fun函数
    fun(per)  # Python中的多态，不关心对象的数据类型，只关心对象是否具有同名的方法
    fun(cat)
    fun(dog)
