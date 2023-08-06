# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

from multiprocessing import Pool
import os
import  time

# 你女儿早读，边叫你起床 ,最后一起吃早餐

def test1():
    print('当前进程ID：{0},它的父进程是:{1}'.format(os.getpid(),os.getppid()))
    print("女叫你起床,你开始慢慢的起来")
    time.sleep(3)
    print("你起来")
    return "abc"


def test2():
    print("女儿开始早读,当前进程是:%s"%os.getpid())
    time.sleep(5)
    print("女儿早读完成")


#test 任务是前面的两个异步任务（test1和test2）,都完成了，才调用test3
def test3(args):
    print("最后一起吃早餐,当前进程的id:%s"%os.getpid())
    print("参数是:%s"%args)

if __name__ == '__main__':
    #女儿使用主进程代表
    #父亲使用进程池中某个子进程代表

    #创建进程池
    pool = Pool(4)
    pool.apply_async(func=test1,callback=test3)  #callback表示回调函数。主进程自动调用的
    #主进程代表女，叫父亲起床之后，继续做自己的早读
    test2()

    print("主进程结束，主进程ID：%s"%os.getpid())





