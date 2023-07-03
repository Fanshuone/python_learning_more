class People:
    num1 = 10
    num1 += 20

    def __init__(self, num2):
        self.num1 += 10
        self.num2 = num2


p01 = People(100)
print('p01.num1:', p01.num1)
print("People.num1:", People.num1)

p02 = People(100)
print('p01.num1:', p02.num1)
print("People.num1:", People.num1)

print(type(p01))


class MyClass:
    class_attr = "Hello, World!"  # 类属性


obj1 = MyClass()
obj2 = MyClass()

print(obj1.class_attr)  # 输出: Hello, World!
print(obj2.class_attr)  # 输出: Hello, World!

obj1.class_attr = "Modified"
print(obj1.class_attr)  # 输出: Modified
print(obj2.class_attr)  # 输出: Hello, World!
print(MyClass.class_attr)  # 输出: Hello, World!
