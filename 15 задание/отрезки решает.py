def f(a1, a2, x):
    return ((a1 <= x <= a2) <= (1 <= x <= 20)) or (5 <= x <= 24)

#1
maxd = -1
for a1 in range(1, 25):
    for a2 in range(1, 25):
        if all(f(a1, a2, x) for x in range(1, 25)):
            maxd = max(maxd, a2 - a1)

print(maxd)


#2
maxd = -1
for a1 in range(1, 25):
    for a2 in range(1, 25):
        flag = True
        for x in range(1, 25):
                if f(a1, a2, x) == 0:
                    flag = False
                    break

        if flag:
            maxd = max(maxd, a2 - a1)

print(maxd)


#3
maxd = 0
for a1 in range(1, 25):
    for a2 in range(1, 25):
        kx = 0
        for x in range(1, 25):
                if f(a1, a2, x):
                    kx += 1
        if kx == (25 - 1):
            maxd = max(maxd, a2 - a1)

print(maxd)