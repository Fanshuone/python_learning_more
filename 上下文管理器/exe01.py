class MyContextManager:
    def __enter__(self):
        # 在进入代码块之前执行的操作
        print("Entering the context")
        # 返回一个值，该值将被绑定到 `as` 关键字后的变量上
        return "Hello, context"

    def __exit__(self, exc_type, exc_value, traceback):
        # 在离开代码块时执行的操作
        print("Leaving the context")
        if exc_type is not None:
            # 处理异常
            print(f"An exception occurred: {exc_type}, {exc_value}")
        # 返回一个布尔值，表示是否要吞掉异常
        return True


# 使用上下文管理器
with MyContextManager() as context:
    print(context)
    # 在此处执行一些操作
    # 如果发生异常，__exit__() 方法会被调用来处理异常
