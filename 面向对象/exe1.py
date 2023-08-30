import types


class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name


if __name__ == '__main__':
    p = Person(23, 'fanshu')

    def run(self, para = "Wood"):
        print(para,"is running",self.name)

    p.run = run
    # p.run = types.MethodType(run,p)
    p.run(p)