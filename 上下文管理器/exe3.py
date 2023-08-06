import traceback as ts


class MyContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving the context")
        if exc_type is not None:
            print(f"An exception occurred: {exc_type}, {exc_value}")
            # 打印异常的追踪信息
            ts.print_tb(traceback)
            return True


# 使用上下文管理器
with MyContextManager():
    1 / 0
