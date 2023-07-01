# coding:utf-8
import json

# 准备高维数据
lst = [
    {'name': '杨淑娟', 'age': 18, 'score': 90},
    {'name': '陈梅梅', 'age': 21, 'score': 89},
    {'name': '李一一', 'age': 19, 'score': 100}
]
# 编码，转成JSON格式，结果为一个字符串
# ensure_ascii=False 正常显示中文
# indent 增加数据的缩进，使用生成的Json格式字符串更具有可读性
s = json.dumps(lst, ensure_ascii=False, indent=4)
print(type(s))
print(s)
# 解码  将JSON格式字符串转成Python中的数据类型
lst2 = json.loads(s)
print(type(lst2))
print(lst2)

# 编码到文件
with open('student.txt', 'w') as file:
    json.dump(lst, file, indent=4, ensure_ascii=False)

# 解码到程序
with open('student.txt', 'r') as file:
    print(json.load(file))
