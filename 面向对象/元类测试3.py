# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

# 第二种写法：自己定义一个元类
class UpperMetaclass(type):

    def __new__(cls, class_name,class_parents,class_attrs):
        # 变量任意一个类所有的属性，把非私有的属性名字改成大写的
        # 定义一个字典保存改完名字之后的属性集合
        new_attrs = {}
        for name, value in class_attrs.items():
            if not name.startswith('__'):  # 判断是否为：非私有的属性
                new_attrs[name.upper()] = value
        # 直接调用type 来创建一个类
        return type.__new__(cls,class_name, class_parents, new_attrs)



# 测试
class Emp(object,metaclass=UpperMetaclass):
    name = 'zhangsan'
    acl = 5000

if __name__ == '__main__':
    print(hasattr(Emp,'name')) #判断Emp类中是否有名字为name
    print(hasattr(Emp,'NAME')) #判断Emp类中是否有名字为NAME
    print(hasattr(Emp,'ACL')) #判断Emp类中是否有名字为ACL