def count_chars(string):
    return string.count('x')

def count_chars_naive(string):
    number_of_x = 0
    for c in string:
        if c == 'x':
            number_of_x += 1
    return number_of_x

assert count_chars("axbxcccxx") == 4
assert count_chars("abc") == 0
assert count_chars_naive("axbxcccxx") == 4
assert count_chars_naive("abc") == 0
