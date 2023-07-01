import time
t = time.time()
print(t)
print(time.localtime(t))
print(time.localtime())
print(time.ctime(t))
print(time.ctime())

print(time.strftime("%Y-%m-%d_%A",time.localtime()))
print(time.strptime("2020-12-21","%Y-%m-%d"))