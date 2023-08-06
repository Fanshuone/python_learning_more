import traceback
class MyContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving the context")
        if exc_type is not None:
            print(f"An exception occurred: {exc_type}, {exc_value}")
            # 处理异常，返回 True 表示异常已经被处理
          
            return True

# 使用上下文管理器
with MyContextManager():
    1 / 0  # 会触发 ZeroDivisionError 异常
