import os
from pprint import pprint


def fun(a, b):
    print("更改前 a id= {} b id= {} ".format(id(a), id(b)))
    a = 3
    print("更改后  a id= {} b id= {} ".format(id(a),id(b)))


x = 1
y = 2

print("x id= {} y id= {} ".format(id(x),id(y)))
fun(x,y)


def hanoi(n, source, target, auxiliary):
    if n > 0:
        # 将n-1个盘子从source移动到auxiliary
        hanoi(n-1, source, auxiliary, target)
        # 将第n个盘子从source移动到target
        print(f"Move disk {n} from {source} to {target}")
        # 将n-1个盘子从auxiliary移动到target
        hanoi(n-1, auxiliary, target, source)

# 测试代码
n = 2
hanoi(n, "A", "C", "B")


pprint(list(os.walk(".")))

print(os.path.abspath('.'))
print(os.path.exists(r'.\\exe04.py'))
print(os.path.basename(r'.\\exe04.py'))
print(os.path.dirname(r'.\\exe04.py'))
