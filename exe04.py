def fun(a, b):
    print("更改前 a id= {} b id= {} ".format(id(a), id(b)))
    a = 3
    print("更改后  a id= {} b id= {} ".format(id(a),id(b)))


x = 1
y = 2

print("x id= {} y id= {} ".format(id(x),id(y)))
fun(x,y)
