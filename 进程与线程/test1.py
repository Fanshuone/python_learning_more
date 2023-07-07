a = b = 10
print(id(a), id(b))

a = 11
b = 11

print(id(a), id(b))

a = 11
b = a

print(id(a), id(b))