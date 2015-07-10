def count_x(string):
    return string.count('x')

def count_x_naive(string):
    number_of_x = 0
    for c in string:
        if c == 'x':
            number_of_x += 1
    return number_of_x

assert count_x("axbxcccxx") == 4
assert count_x("abc") == 0
assert count_x_naive("axbxcccxx") == 4
assert count_x_naive("abc") == 0
