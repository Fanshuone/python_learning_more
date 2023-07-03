# coding:utf-8
class Student:
    # 类属性的:类中，方法外的变量
    school = '北京马士兵教育'

    # 初始方法__init__
    def __init__(self, xm, age):  # xm,age，是方法的参数，局部变量
        # =左侧是实例属性，=右侧是局部变量
        self.name = xm  # 将局部变量的值赋给实例属性self.name
        self.age = age  # 实例属性的名称与局部变量的名称相同了

    # 实例方法
    def show(self):
        print(f'我叫:{self.name},今年:{self.age}岁了')

    # 类方法
    @classmethod
    def cm(cls):
        print('这里是一个类方法，不能调用实例属性和实例方法的')

    # print(self.name)
    # self.show()

    # 静态方法
    @staticmethod
    def sm():
        print('这里是一个静态方法，不能调用实例属性和实例方法')
    # print(self.name)
    # self.show()


# 类的组成部分的使用
# 创建对象  # 在创建对象时，自动调用__init__方法
stu = Student('ysj', 18)  # 只能传2个，为什么，因为__init__方法中自定义的变量有2个
# 使用实例属性,使用对象名，打点使用
print(stu.name, stu.age)
# 使用类属性，使用类名打点使用
print(Student.school)

# 使用对象名打点调用实例方法
stu.show()
# 使用类名打名调用类方法
Student.cm()

# 使用类名打点调用静态方法
Student.sm()
