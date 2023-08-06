import time
import concurrent
start = time.perf_counter()


finish = time.perf_counter()

print(round(finish-start,2))

print(f"you are just a primarier {round(finish-start,2)}")

a = 2000000
b = a
print(id(a))
print(id(b))

a = 10
print(b)
print(id(a))
print(id(b))


a = [print(1) for i in range(10)]
print(a)
open

a = 10
def fun():
    global a
    a+=10
    print(a)

fun()