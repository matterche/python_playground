def is_multiple_of(a, b):
    return a % b == 0


assert is_multiple_of(3, 3)
assert not is_multiple_of(4, 3)
assert not is_multiple_of(5, 3)
assert is_multiple_of(6.6, 3.3)
assert not is_multiple_of(6.1, 3.2)
assert is_multiple_of(2 << 1024, 2 << 1024)
