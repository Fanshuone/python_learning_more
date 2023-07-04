# coding:utf-8
# coding:utf-8
class Person:  # 默认继承了object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫:{self.name}，我今年:{self.age}岁了')


# Student类继承Person类
class Student(Person):
    # 编写初始化方法
    def __init__(self, name, age, stuno):
        # 调用父类的初始化方法
        super().__init__(name, age)  # 给name和age进行赋值
        self.stuno = stuno  # 给自己特有的属性进行赋值

    # 重写父类的方法
    def show(self):
        # 可以去调用父类的show方法，也可以重写编写实现方法的代码，显示输出内容
        # 调用父类的方法
        super().show()
        # 再编写自己个性化的内容
        print(f'我来自马士兵教育，我的学号是:{self.stuno},我的名字是{self.name}')


# Doctor类继承Person类
class Doctor(Person):
    def __init__(self, name, age, department):
        # 调用父类的初始化方法
        Person.__init__(self, name, age)  # 给name,age进行赋值
        self.department = department  # 给自己特有的属性进行赋值

    def show(self):
        # 重新编写方法的实现代码
        print(f'大家好，我叫:{self.name},我今年:{self.age}岁了，我的工作科室是:{self.department}')


if __name__ == '__main__':
    # 创建Student类的对象
    stu = Student('陈梅梅', 20, 'msb1001')
    stu.show()

    # 创建Doctor类的对象
    doctor = Doctor('张一一', 32, '外科')
    doctor.show()
