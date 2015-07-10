x = "global"


def f():
    x = "local_at_f_but_enclosing_for_nested_functions"

    def g():
        x = "some_local"
        func = lambda x: x
        print "in g:", x, func("a")

    print "in f:", x
    print "locals: ", locals()
    print "globals: ", globals()

    g()


f()


# there are no block scopes
for i in range(10):
    pass
print "block scope panic 1: ", i

[x for x in range(10)]
print "block scope panic 2: ", x


def make_global():
    global x
    x = "set from f()"


class A:
    b = 1

    def __init__(self):
        pass

    def f(self):
        self.b += 1  # 1. self.b does not exist => A.b is lookup result 2. result of A.b + 1 is stored in self.b
        print self.b, A.b

    def g(self):
        A.b += 1
        print self.b, A.b

    print b

# be aware of shadowing
round = lambda s: 666  # shadows round function in __builtins__

print round(5.5)

# wow
__builtins__.True = False

print "True: ", True

__builtins__.raw_input = lambda s: "you lost"
print raw_input("Hihi")
