def f(x, y):
    A = 3 <= x <= 60
    B = 177 % x == 0 and x != 177 and x != 1
    C = y % x == 0 and x != y and x != 1
    return (C) <= ((A) and (not (B)))

for y in range(1, 10000):
    if any(y % x == 0 for x in range(2, y))\
            and all(f(x, y) for x in range(1, 10000)):
        print(y)

# или

def f(x, y):
    A = 3 <= x <= 60
    B = 177 % x == 0 and x != 177 and x != 1
    C = y % x == 0 and x != y and x != 1
    return (C) <= ((A) and (not (B)))

for y in range(1, 10000):
    d = [x for x in range(2, y) if y % x == 0]
    if d and all(f(x, y) for x in range(1, 10000)):
        print(y)