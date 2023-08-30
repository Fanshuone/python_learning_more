# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
class Person(object):
    # age 属性的值限制的范围是0——88
    def get_age(self):
        return self._age

    def set_age(self, value):
        if 0 <= value <= 88:
            self._age = value
        else:
            # print("age的值必须在0到88之间")
            self._age = 0  # 0为age的初始值
            raise ValueError('age的值必须在0到88之间')


class Person_Property(object):

    # age 属性的值限制的范围是0——88
    @property  # age 属性暴露出去
    def age(self):
        return self._age

    @age.setter  # 当前age属性可以允许赋值
    def age(self, value):
        if 0 <= value <= 88:
            self._age = value
        else:
            # print("age的值必须在0到88之间")
            self._age = 0  # 0为age的初始值
            raise ValueError('age的值必须在0到88之间')

    @property
    def name(self):
        self._name = "张三"
        return self._name


if __name__ == '__main__':
    p = Person_Property()
    p.age = 18
    print(p.age)  # age属性可以读，可以写
    # p.name = "Lisi"
    print(p.name)  # name属性是只读的
