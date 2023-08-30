class Logs(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, fun):
        def wrapped_function(*args, **kwargs):
            log_string = fun.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
                # 现在，发送一个通知
                self.notify()
            return fun(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # Logs只打日志，不做别的
        print("--------------------------")


@Logs()
def decor_a():
    print("log开始")


decor_a()
print(decor_a.__name__)

int()