def f(x, a):
    return ((x % a != 0) and (x % 24 == 0)) <= ((x % 16 != 0) or (x % 24 != 0))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)