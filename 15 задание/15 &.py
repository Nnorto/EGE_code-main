def f(a, x):
    return (x & a != 0) <= ((x & 10 == 0) <= (x & 3 != 0))

#1

for a in range(1, 1000):
    kx = 0
    for x in range(1, 1000):
        if f(a, x):
            kx += 1
    if kx == (1000 - 1):
        print(a)


#2

for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if f(a, x) == 0:
            flag = False
            break
    if flag:
        print(a)



#3

for a in range(1, 1000):
    for x in range(1, 1000):
        if f(a, x) == 0:
            break
    else:
        print(a)


#4

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
