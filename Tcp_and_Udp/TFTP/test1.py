rb = b'\xff\xd8'
print(bytes(0))
print(len(rb))

import struct

# 将字符串打包成字节序列
string_data = "Hello, World!"
encoded_data = string_data.encode('utf-8')  # 使用 UTF-8 编码将字符串编码为字节串
packed_data = struct.pack(f'{len(encoded_data)}s', encoded_data)  # 使用格式指令将编码后的字节串打包
print(encoded_data)
print(packed_data)

import struct

# 将字符串和数字联合打包成字节序列
string_data = "Hello"
number = 42
encoded_data = string_data.encode('utf-8')  # 使用 UTF-8 编码将字符串编码为字节串
packed_data = struct.pack(f'{len(encoded_data)}sI', encoded_data, number)  # 使用格式指令将字符串和数字打包
print(packed_data)
print(packed_data.decode(encoding='utf-8'))

print(number.to_bytes(6, 'big'))

print("abc".encode("utf-8"))

try:
    a = 1
    print(1 / 0)
except Exception as e:
    print(e)

print(a)

import traceback



try:

    y = 1 / 0

except:
    traceback.print_exc()



print(1111)

print(1 / 0)

print(1111)