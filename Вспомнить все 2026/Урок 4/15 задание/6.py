def f(x, y, a):
    return ((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9))
for a in range(0, 1000):
    if all(f(x, y, a) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
