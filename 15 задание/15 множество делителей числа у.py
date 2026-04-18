def f(x, y):
    A = 6 <= x <= 52
    B = 153 % x == 0 and x != 1 and x != 153
    C = y % x == 0 and x != 1 and x != y
    return (C) and ((A) <= (B))

for y in range(1, 10000):
    if any(y % x == 0 for x in range(2, y)):
        if all(f(x, y) == 0 for x in range(1, 10000)):
            print(y)