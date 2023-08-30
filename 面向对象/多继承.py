# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

class Father(object):
    def work(self):
        print("父亲在工作")

class Mather(object):
    def work(self):
        print("母亲在工作")

class Child(Mather,Father): # 多继承
    def __init__(self,xname):
        self.name = xname

    def work(self):
        print("自己在工作")


if __name__ == '__main__':
    c = Child('张三')
    c.work() # 如果多个父类中都有同样的函数，按照优先级来调用
    print(Child.__mro__) # 打印Child的继承结构，并且按照优先级
