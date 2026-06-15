def f(x, a):
    return (x % a == 0) or ((40 <= x <= 50) <= (x % 12 != 0))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)

