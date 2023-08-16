# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

from greenlet import greenlet


# 开发协程的案例，一个任务是回答，一个任务是问

def ask(name):
    print("%s : 我要买个手提包！" % name)  # 2
    b.switch("吕布")  # answer函数第一次切换，需要传参
    print("%s : 我想要学个Python！" % name)  # 4
    b.switch()


def answer(name):
    print("%s : 买买买！！" % name)  # 3
    a.switch()
    print("%s :可以买，一定去马士兵教育!" % name)


if __name__ == '__main__':
    a = greenlet(ask)  # 创建一个协程
    b = greenlet(answer)  # 创建第二个协程
    a.switch('貂蝉')  # 每个函数只有在第一次切换的时候才需要传参，后面不需要  #1
