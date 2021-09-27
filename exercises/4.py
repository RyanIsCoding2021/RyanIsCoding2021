prev = 0

for i in range(10):
    print("{} + {} = {}".format(i, prev, i + prev))
    prev = i   