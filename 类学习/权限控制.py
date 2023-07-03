# coding:utf-8
class Student():
    # 首尾双下划线,表示特殊的方法，系统定义
    def __init__(self, name, age, gender):
        self._name = name  # 以单下划线开头，表示是受保护的成员，只能类本身和子类访问
        self.__age = age  # 以双下划线开头，表示是私有的，只能类本身使用
        self.gender = gender  # 普通的实例属性，在类的外部和类的内部以及子类都可以访问

    def _fun1(self):  # 以单划线开头，表示是受保护的方法
        print('子类和本身可以访问')

    def __fun2(self):  # 以双下划线开头，表示的是私有的
        print('只有定义的类可以访问')

    # 这是一个普通的实例方法，在类的外部使用对象名打点访问
    # 在类的内部，使用self打点访问
    def show(self):
        self._fun1()  # 类本身访问受保护的方法
        self.__fun2()  # 类本身访问私有的方法
        print(self._name)  # 类本身访问受保护的实例属性
        print(self.__age)  # 类本身访问私有的实例属性


if __name__ == '__main__':
    # 创建一个Student类型的对象
    stu = Student('陈梅梅', 20, '女')
    # 访问受保护的实例属性
    print(stu._name)
    # 访问私有的实例属性
    # print(stu.__age) #程序报错，出了类的定义范围

    # 访问受保护的实例方法
    stu._fun1()
    # 访问私有的实例方法
    # stu.__fun2()

    # 可以使用以下的形访问类对象的私有成员
    print(stu._Student__age)

    stu._Student__fun2()
