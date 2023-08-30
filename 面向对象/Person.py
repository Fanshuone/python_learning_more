# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import types


class Person(object):

    def __init__(self, x_name, x_age):
        self.name = x_name
        self.age = x_age


# 限制类动态增加属性
class Student(object):
    # 只允许当前Student拥有name和sex属性
    __slots__ = ('name', 'sex')


if __name__ == '__main__':
    p = Person('zhangsan', 23)
    # 1、 可不可以动态的给对象p赋予一个新的对象属性
    Person.address = "北京"
    p.sex = '男'
    print(p.sex)


    # 2、 可以给当前对象p 动态的赋予一个新的对象函数吗

    def run(self, work):
        print('%s正在完成的工作是:%s' % (self.name, work))


    p.run = types.MethodType(run, p)  # 给对象p添加一个实例（成员，对象）函数
    p.run('学习')


    # 3、给Person类动态赋予一个类函数
    @classmethod
    def class_run(cls, work):
        print("类函数中的work是:%s" % work)


    Person.work = class_run
    p.work('学习python')


    # 4、 给Person类动态赋予一个静态函数
    @staticmethod
    def static_run(work):
        print('静态函数中的work是:%s' % work)


    Person.staticRun = static_run
    p.staticRun('学习全栈')
    Person.staticRun('学习全栈')

    # 验证slots
    s = Student()
    s.name = 'lisi'
    s.sex = '女'
    # Student.age =10 类属性没有限制 ，可以动态添加
    # s.age =23
    print(s.age)
