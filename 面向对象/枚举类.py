# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

# 当项目中需要使用12个月份时
# Jan =1
# Feb =2
# ...

from enum import Enum

# 枚举中：一个名字 对应一个值 第一种：定义一个枚举
Month = Enum('Month',('jan','feb','mar','apr','may','jun','jul'))

# 把整个枚举中的所有值遍历出来
print(Month.__members__) # 枚举中的值自动从1开始，不会重复

#得到二月份的值
print(Month['feb'].value)

# 根据值(2)来得到月份的名字
print(Month(2).name)


# 定义一个颜色的常量枚举
class Color(Enum): # 第二种：自定义一个枚举类
    red = 100
    green =200
    blue =30
    yellow =200 # 不允许key相同或者value。如果value重复了根据value取name只能得到第一个

print(Color(200))