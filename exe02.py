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


