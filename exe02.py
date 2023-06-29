import random

a = b = 1
print(id(a), id(b))
b = 2
print(id(a), id(b))

c = d = [2, 5, 4]
print(id(c), id(d))
c[0] = 3
print(id(c), id(d))
print(c, d)

# c[4] = 10  # 报错 list assignment index out of range
# print(c,d)

# 列表生成试

list1 = [random.randint(0, 100) for i in range(10)]
print(list1)

str1 = "abcd bacd bdca abcd bcba"

print(str1.strip('ab'))

a = 2
b = 3
if a == 2:
    print(2)
    if b == 3:
        print(4)
else:
    print(2)


def fun1(*args):
    print(args)


fun1(1, 2)


def fun2(**kwargs):
    print(kwargs)
    return kwargs['a'], kwargs['b']


c = fun2(a=1, b=2)
print(c)

# list 的 sort 函数中关键字参数key是将列表中的元素按照key中的方法进行转换后，按照转换后的元素进行排序
# key的参数一般是lambda表达式

print(str.lower("FSDFA"))

# lambda 函数 相当于一个只有返回值的函数
# lambda x,y: 有关x,y的表达式  # 这个表达式就是一个返回值

# 迭代器

a = [10, 20, 30]

print(next(iter(a)))

# filter函数
"""
 filter(function or None, iterable) --> filter object
    
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """


def fun2(num):
    return num % 2 == 1


list2 = list(range(10))

print(list2)
print(list(filter(fun2, list2)))

# map函数
"""
    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    """


def fun3(num):
    return num+1


print(list(map(fun3,a)))

# 条件表达式语法
print("在" if 1 else '不在')

with open()