# 原始对象
original_list = [1, 2, [3, 4]]

a = original_list
print("a id = ",id(a))
print("original_list id = ",id(original_list))

original_list[0] = 2
print("a id = ",id(a))
print("original_list id = ",id(original_list))

print("a",a)
print("original_list: ",original_list)


b = 2
c = b

print("id b ",id(b))
print("id c ",id(c))