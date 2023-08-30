# a = ()
# print(a[0])
import time


def main_logger(log_file='out.log'):
    def logger(func):
        def write_logging(*args, **kwargs):
            log = '[info] --时间是：%s' % time.strftime("%H:%M:%S", time.localtime())
            print(log)
            with open(log_file, 'a') as f:
                f.write(log+'\n')
            func(*args, **kwargs)
            print("写入完成")

        return write_logging

    return logger


@main_logger()
def work1():
    print("开始第一次写入")


@main_logger()
def work2(*args, **kwargs):

    print("开始第一次写入%d %d" % (args[0], args[1]))



work1()
work2(1,2)

print(work1.__name__)