# escaping vs. quotes vs. ticks

print " \"WHEE\" "
print ' \'WHOO\' '
print " 'WHOO' "
print ' "WHAA" '
print '''
    "WHAA"
        "WHOOM"
'''

# raw string -> backslahes are not interpreted -> useful for regex
print r" \"RAW\" "

# no arrays, a list is a sequence
list = ['a', 'b', 'c', 'd']
print list[0], list[1], list[2], list[3]
print list[-1], list[-2], list[-3], list[-4]

# a string is a sequence
string = 'efgh'
print string[0], string[1], string[2], string[3]
print string[-1], string[-2], string[-3], string[-4]

# dictionary can hold arbitrary types
def func():
    print "hello world"

dic = {
    '1': 2,
    'a': [1, 2, 3],
    1: 'a',
    'fun': func
}

print dic
