def f(x, y):
    A = 7 <= x <= 26
    B = 77 % x == 0 and x != 1 and x != 77
    C = y % x == 0 and x != 1 and x != y
    return (C) <= ((A) and (not(B)))

for y in range(1, 1000):
    d = [x for x in range(2, y) if y % x == 0]
    if d and all(f(x, y) for x in range(1, 1000)):
        print(y)
        break
