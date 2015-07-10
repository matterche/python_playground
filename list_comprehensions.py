result = []
for i in range(10):
    if i > 5:
        result.append(i + 2)

print result

result = map(lambda x: x + 2, filter(lambda y: y > 5, range(10)))

print result

result = [x + 2 for x in range(10) if x > 5]

print result

# (3*x) in if is needed when comparison should be done after multiplication
print [3 * x for x in range(10) if (3 * x) < 4]
