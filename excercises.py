# double every character in a string
def double_chars1(s):
    b = ""
    for i in s:
        b += i * 2
    return b


def double_chars2(s):
    l = list(s)
    for i in range(len(l)):
        l[i] *= 2
    return "".join(l)


def double_chars_functional(s):
    return "".join(map(lambda c: c * 2, s))


def double_chars_functional_comprehension(s):
    return "".join([2 * x for x in s])


def double_chars_functional_without_join(s):
    return reduce(lambda st1, st2: st1 + st2, map(lambda c: c * 2, s))


assert double_chars1("abc") == "aabbcc"
assert double_chars2("abc") == "aabbcc"
assert double_chars_functional_comprehension("abc") == "aabbcc"
assert double_chars_functional("abc") == "aabbcc"
assert double_chars_functional_without_join("abc") == "aabbcc"


# implement swapcase
assert "AbCd".swapcase() == "aBcD"


def swapcase(s):
    res = ""
    for c in s:
        res += c.upper() if c.islower() else c.lower()
    return res


assert swapcase("AbCd") == "aBcD"
