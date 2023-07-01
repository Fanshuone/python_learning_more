class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        # 获取资源或执行其他设置操作
        # 返回资源

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # 释放资源或执行其他清理操作
        # 处理异常（如果有）

# 使用上下文管理器
with MyContextManager() as cm:
    pass
    # 在这里可以使用获取到的资源
    # 执行其他操作

# 在退出上下文后，资源已被正确释放

tu = ([1,2], [3,4])
print(type(tu))
tu1 = tu[1:]



print('tu1 ',tu1)
print(type(tu1))

tu[1][0] = 12

print('tu1 ',tu1)
print(tu)

open()