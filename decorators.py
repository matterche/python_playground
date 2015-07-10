# decorators wrap functions (function or classname) aka aspect oriented programming
# must always return the function
# use cases: logging, caching, security
def mydecorator(func):
    print "inside the mydecorator with function", func
    return func


def decorator_closure(func):
    my_string = "func executed in decorator_closure and returned "

    # args can be modified
    def wrapper(*args):
        print "in wrapper", args
        ret = func(*args)
        print my_string, ret

    return wrapper


@mydecorator
def bar(param):
    print "bar ", param


@decorator_closure
def bor(param):
    print "bor ", param
    return "bor"


bar("1")

bor("2")
