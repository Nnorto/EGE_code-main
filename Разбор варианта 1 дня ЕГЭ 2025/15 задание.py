def f(x, y, a):
    return (x * y > a) or (x > y) or (11 > x)

for a in range(0, 1000):
    if all(f(x, y, a) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)