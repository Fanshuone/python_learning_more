"""
在上述示例中，calculate_area 是一个类方法，它通过类名 MathUtils 直接调用，并且可以访问类属性 PI。

相比之下，add_numbers 是一个静态方法，它可以通过类名 MathUtils 或实例对象调用，但不能访问类属性。

总结来说，类方法和静态方法在不同的情况下有不同的用处。类方法用于与类本身相关的操作，而静态方法用于与类或实例无关的功能。

它们提供了更灵活和组织性的方式来编写和管理类中的相关功能。
"""


class MathUtils:
    PI = 3.14159  # 类属性

    @classmethod
    def calculate_area(cls, radius):
        cls.PI = 10
        cls.PP = 11
        return cls.PI * radius ** 2

    @staticmethod
    def add_numbers(x, y):
        return x + y


# 调用类方法
print(MathUtils.PI)

area = MathUtils.calculate_area(5)
print(area)  # 输出: 78.53975
print(MathUtils.PI)
print(MathUtils.PP)  # 可以在类中先定义类属性，再在类方法中更改类属性

# 调用静态方法
result = MathUtils.add_numbers(3, 4)
print(result)  # 输出: 7


print(MathUtils().PI)