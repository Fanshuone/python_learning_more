# coding:utf-8
#  dir 能够查询类中所有的属性和方法

print(dir(object))


# Person默认继承object类，所以object可以省略不写
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫:{self.name}，今年{self.age}岁了')

    # 重写__str__方法
    def __str__(self):
        return '这是一个人类，具有name和age两个实例属性'


if __name__ == '__main__':
    # 创建了一个Person类型的对象
    per = Person('陈梅梅', 20)
    print(dir(per))
    print('------------------')
    print(per)  # 当直接输出对象名时，默认调用__str__()方法
    print(per.__str__())
    print('----------------------------')
    # Person类的对象，调用父类的__dir__方法
    # 以下这两句代码功能相同，
    print(per.__dir__())
    print(dir(per))
