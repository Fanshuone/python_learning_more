# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
# 引入模块，需要模块的路径

# 第一种：
# from 面向对象的进阶.元类 import Person
# from 引入模块之后，则动态的创建了一个Person类 ，本质上python解释器自动调用了type()来创建一个Person

# def func(self, words='hello'):
#     print("我说:%s" % words)

#第二种： 使用type() 创建一个Person类,其实创建任何一个类型
# Person = type('Person',(object,),dict(say =func))


#第三种：使用一个metaclass来创建一个Person类
class PersonMetaclass(type): # 所有的元类必须继承type

    def __new__(cls, name,bases,attrs):
        def func(self, words='hello'):
            print("我说:%s" % words)
        attrs['say'] = func
        return type.__new__(cls,name,bases,attrs)
# 根据上面的元类，创建一个Person类, (首先需要一个模具，然后在生产产品)
class Person(object,metaclass=PersonMetaclass):
    pass

p = Person() # 创建一个Person类的实例

p.say('hello')

print(type(p)) # 把实例p的类型打印出来

print(type(Person)) # Person类的类型打印 ,本质上就是打印创建了Person类的元类

# type()函数,使用用于创建类的函数
a =19
print(a.__class__.__class__) # 打印a变量的类型的类型
