def f(a, x, y):
    return ((y * y <= a) <= (y < 12)) and ((x < 11) <= (x*x < a))

#1

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break

#2

for a in range(1, 500):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            if f(a, x, y) == 0:
                flag = False
                break

    if flag:
        print(a)
        break

#3

for a in range(1, 501):
    kxy = 0
    for x in range(1, 500):
        for y in range(1, 500):
            if f(a, x, y):
                kxy += 1
    if kxy == ((500 - 1)*(500-1)):
        print(a)
        break
