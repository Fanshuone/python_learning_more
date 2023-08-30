# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

class Person(object):

    def __init__(self,xname):
        self.name = xname
        # 斐波拉契数列前两个值是固定
        self.a ,self.b = 0,1

    # 用于定制对象的描述信息
    def __str__(self):
        return "Person object (name :%s)"%self.name

    # person默认不是可迭代对象,变成一个可迭代对象，必须返回一个迭代器
    def __iter__(self):  # 生成一个斐波拉契数列
        return self

    # person就变成一个迭代器
    def __next__(self):
        self.a ,self.b = self.b, self.a+self.b # 计算下一个值
        if self.a > 1000: # 如果出现一个大于1000的数字，退出循环
            raise StopIteration
        return  self.a

    # person就可以类似于list
    def __getitem__(self, item): # item 可能是一个下标，还有可能是一个切片（范围）
        if isinstance(item,int): # item是一个下标
            a,b =1,1
            for x in range(item):
                a ,b = b,a+b
            return a
        elif isinstance(item,slice): # item是一个范围
            start = item.start
            stop = item.stop
            if start is None:
                start = 0 # start默认值
            a,b =1,1
            L = []
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b =b,a+b
            return L

    # 当访问person对象中不存在的属性和函数的时候会抛出AttributeError，如果不想看到这个error则需要重写
    def __getattr__(self, item):
        if item =='age':
            return 18
        elif item == 'eat':
            return lambda : print('eat函数执行')

    def __call__(self, *args, **kwargs):
        print('person 对象可以调用')

if __name__ == '__main__':
    p = Person('张三')
    print(p)

    for n in p:
        print(n)

    # p 有的类似于一个list，在list还可以切片
    print("下标为5的值是:",p[5])
    print("下标为5-10的值是:",p[5:10])

    print(p.age)
    p.eat()

    p() #把person对象当成一个函数，直接调用，person对象 ==一个函数

    print(callable(p)) # 判断出来p对象，是不是可以调用的对象 （函数）