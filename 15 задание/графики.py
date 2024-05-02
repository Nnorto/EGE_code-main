def f(a, x, y):
    return (x * y < 140) or (y > a) or (x > a)

#1

for a in range(1, 250):
    if all(f(a, x, y) for x in range(1, 500) for y in range(1, 500)):
        print(a)



#2

for a in range(1, 250):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            if f(a, x, y) == 0:
                flag = False
                break

    if flag:
        print(a)


#3

for a in range(1, 250):
    kxy = 0
    for x in range(1, 500):
        for y in range(1, 500):
            if f(a, x, y):
                kxy += 1
    if kxy == ((500 - 1)*(500-1)):
        print(a)
