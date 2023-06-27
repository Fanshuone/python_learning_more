# is 和 == 的区别
# is 表示内存地址相同； == 表示值相同
a = 10
b = 10
print(a == b)
print(id(a), id(b))
print(a is b)
a += 1
print(id(a), id(b))
print(a is b)

# 条件表达式 if else 的简写
print("ab" if 3 > 1 else "bc")  # 结构 x if 判断条件 else y

# for 循环 和 while 循环 中最后加else,是可以在循环后执行的（没有break）
a = 1
while a < 5:
    print(a)
    a += 1
    if a == 4:
        # break
        continue
else:
    print(a)

# 二重循环里面的break 和 continue 用于控制本层循环



