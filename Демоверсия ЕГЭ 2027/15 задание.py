def f(x, a):
    B = 70 <= x <= 90
    return (x % a == 0) or ((B) <= (x % 22 != 0))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)