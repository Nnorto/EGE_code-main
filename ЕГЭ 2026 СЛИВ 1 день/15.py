def f(x, a):
    return ((x % 2 == 0) <= (x % 3 == 0)) or (x + a >= 80)
for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)
        break

#####
def f(x, a):
    b = 50 <= x <= 60
    return (x % a == 0) or ((b) <= (x % 13 != 0))


for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)

