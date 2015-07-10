# -*- coding: utf-8 -*-
# needed for editors, mandatory when using umlauts


# get help
help(map)
dir(__builtins__)
a = []
dir(a)
help(a)
type([])

# escaping vs. quotes vs. ticks
print " \"WHEE\" "
print ' \'WHOO\' '
print " 'WHOO' "
print ' "WHAA" '
print '''
    "WHAA"
        "WHOOM"
'''


# raw string -> backslashes are not interpreted -> useful for regex
print r" \"RAW\" "

# Python doesn't know arrays, a list is a sequence with arbitrary types
def func_list():
    print "hello world"


a_list = ['a', 'b', 'c', 'd', 2, 3, func_list]
print a_list[0], a_list[1], a_list[2], a_list[3]
# navigate list from end
print a_list[-1], a_list[-2], a_list[-3], a_list[-4]

# a string is a sequence
string = 'efgh'
print string[0], string[1], string[2], string[3]
print string[-1], string[-2], string[-3], string[-4]

# dictionary can hold arbitrary types including functions
# for correct hashing, dictionary keys must be immutable -> String, Tuple, FrozenSet
dic = {
    '1': 2,
    'a': [1, 2, 3],
    1: 'a',
    100: 101,
    'fun': lambda foo: foo + 1,
    (1, 2, 3): "Tuple Key"
}


# print is a statement and doesn't need parentheses
print 100 in dic

"""
this is a
 multiline
docstring
"""

# basestring can be unicode string or standard string
isinstance("bla", basestring)

# list comprehension
len([x for x in "bxb" if x == 'x'])


# if, elif, else
if 1 in [1, 2]:
    print "hello"
elif 3 in [1, 2]:
    pass
else:
    pass

# for loops
for i in range(10):
    print i
else:
    # called when no break exits the loop
    print "the end1"

# tuple assignment
a, b = 1, 2

a, b = b, a

a, b = 1 + 1, "axb".count('x')



# ternary operator equivalent
def bla(n):
    return n if n in [0, 1] else 100

# 'is' compares references
# '==' is deep equals but must be implemented by comparator
a = []
b = a
c = []
a == c  # True
a == b  # True
a is b  # True
a is c  # False

a = 3
b = 3

True == a is b

# try:
#     import foo
# except
#     foo = MyFoo()

# magic methods and operator overloading
# __init__
# __len__ -> with naming conventions operator overloading is possible

# tuple with one element
a = (1,)

# replace elements in a list
a = range(10)
a[1::4] = [None] * 3

# remove elements via pop()
a.pop()
a.pop(0)
a.pop(3)



# function definitions
def funky(aa, bb="optional", *args, **keywords):
    print aa, bb
    print args
    print keywords


def drunky(p1, p2, p3):
    print "in g", p1, p2, p3


drunky(*[1, 2, 3])
drunky(**{"p1": 4, "p2": 5, "p3": 5})

funky(1)
funky(1, 2)
funky(1, 2, 3, 4, 5)
funky(1, 2, 3, 4, 5, ai=6, xy=[1, None])

lamm = lambda la: la + 1
print lamm(24)

arr = [1, 2, 3]
map(lambda ch: str(ch), arr)
map(str, arr)

"""
Questions
 * is method overloading possible?
 * automatic type conversions
"""

# support starting from command line
if __name__ == "__main__":
    s = raw_input("give me 1: ")
    # assert with message
    assert s == "1", 's is not 1'

# react on Ctrl+C
try:
    raw_input("Give me some input")
except KeyboardInterrupt:
    import sys  # can be done everywhere

    sys.exit(1)
