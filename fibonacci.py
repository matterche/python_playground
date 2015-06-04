def fibonacci():
    f1 = -1
    f2 = 0
    while True:
        if f1 == -1:
            f1 = 1
            yield 0

        result = f1 + f2
        f1 = f2
        f2 = result
        yield result
    return


fibu_expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

generator = fibonacci()
for i in range(21):
    assert fibu_expected[i] == generator.next()
