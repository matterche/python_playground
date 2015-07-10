# generators are functions which return a set of values where elements are only evaluated when they are needed.
# lazy lists
# can be compared to Scala streams

def first_ten_even():
    current = 0
    while current < 20:
        yield current
        current += 2


generator = first_ten_even()

for i in first_ten_even():
    print i
