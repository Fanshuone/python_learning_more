# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import threading

import time, os


def run(name):
    for i in range(3):
        print("线程名字%s,输出:%d" % (name, i))
        time.sleep(1)


if __name__ == '__main__':
    print("主线程开始时间:%s" % time.time())

    # 创建多个线程
    s = "abcdef"
    for i in range(5):
        t = threading.Thread(target=run, name=s[i], args=(s[i],))  # 创建线程
        # t = threading.Thread(target=run, args=(s[i],))
        # print(t.name)
        t.start()  # 启动线程

    print('主线程结束')
