# def my_filter(n):
#     return lambda x: x % n > 0

def fun():
    pass


def my_filter(n):
    return lambda x: x % n > 0


a = filter(my_filter(5), [2, 3, 5, 7, 11])

print(list(a))
