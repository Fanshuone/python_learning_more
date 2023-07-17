with open("1.txt",'r') as f:
    while 1:
        data = f.read(10)
        if not data:
            break
        print(data,end="")

print(len(b'asdf'))