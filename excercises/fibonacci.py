def fibonacci(max_results):
    f1 = -1
    f2 = 0
    for x in range(max_results):
        if f1 == -1:
            f1 = 1
            yield 0

        result = f1 + f2
        f1 = f2
        f2 = result
        yield result
    return


def fibonacci_recursive(actual=[0, 1], f1=0, f2=1, max_result=7000):
    result = f1 + f2

    if result > max_result:
        return actual

    actual.append(result)
    return actual + fibonacci_recursive(actual, f2, result)


fibonacci_expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

fibonacci_generator = fibonacci(20)
fibonacci_rec = fibonacci_recursive()

print fibonacci_rec

for i in range(21):
    assert fibonacci_expected[i] == fibonacci_generator.next()
    assert fibonacci_expected[i] == fibonacci_rec[i]
