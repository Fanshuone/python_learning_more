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

    @classmethod
    def change_school(cls):
        cls.school = '北京马士兵教育贵'


# 创建N多个对象
stu = Student('ysj', 18)
print(Student.school)
stu2 = Student('陈梅梅', 20)
Student.change_school()
print(Student.school)
stu3 = Student('马丽', 23)
stu4 = Student('Marry', 21)
print(type(stu))
print(type(stu2))
print(type(stu3))
print(type(stu4))
Student.school = '马士兵教育'
print(stu.name, stu.age)

# 将对象放到组合数据类型中存储，存储到列表中
lst = [stu, stu2, stu3, stu4]
for item in lst:  # item的数据类型为Student，item是一个Student类型的对象
    item.show()  # 对象名,打点调用实例方法
