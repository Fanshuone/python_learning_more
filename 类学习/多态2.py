class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# 创建不同的对象
rectangle = Rectangle(5, 3)
circle = Circle(2)

# 调用相同的方法，但根据对象的实际类型，会调用不同的具体实现
print(rectangle.area())  # 输出: 15
print(circle.area())  # 输出: 12.56
