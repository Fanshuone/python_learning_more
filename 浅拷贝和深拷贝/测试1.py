import copy

# 原始对象
original_list = [1, 2, [3, 4]]

# 浅拷贝
shallow_copy = copy.copy(original_list)

print("id original_list ",id(original_list))
print("id shallow_copy ",id(shallow_copy))
# 修改原始对象的子对象
original_list[2][0] = 5
original_list[1] = 5
# 输出结果
print(original_list)   # [1, 2, [5, 4]]
print(shallow_copy)    # [1, 2, [5, 4]]
