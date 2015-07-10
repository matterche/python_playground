a = range(10)

# old school
for i in range(len(a)):
    index, item = i
    pass


# better
for i in enumerate(a):
    index, item = i
    pass

# even shorter
for index, item in enumerate(a):
    pass

m = {"1": "1.1"}

for k, v in m.items():
    pass

# better
for name, price in enumerate(m.items()):
    pass
