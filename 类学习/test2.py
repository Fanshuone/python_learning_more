class C1():
    def fun_c1(self):
        print("傻叉")


class C2():
    def fun_c1(self):
        print("二货")


class C_Child(C1):

    pass


ex = C_Child()
ex.fun_c1()