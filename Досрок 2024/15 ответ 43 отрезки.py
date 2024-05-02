def f(a1, a2, x):
    return (47 <= x <= 115) <= ((not(a1 <= x <= a2) and (24 <= x <= 90)) <= (not (41 <= x <= 115)))


# 1 способ
mind = 10 ** 10

for a1 in range(20, 120):
    for a2 in range(a1+1, 120):
        if all(f(a1, a2, x) for x in range(20, 120)):
            mind = min(mind, a2 - a1)

print(mind)

# 2 способ
mind = 10 ** 10
for a1 in range(20, 120):
    for a2 in range(a1+1, 120):
        flag = True
        for x in range(20, 120):
            if f(a1, a2, x) == 0:
                flag = False
                break

        if flag:
            mind = min(mind, a2 - a1)

print(mind)

# 3 способ
mind = 10 ** 10
for a1 in range(20, 120):
    for a2 in range(a1+1, 120):
        for x in range(20, 120):
            if f(a1, a2, x) == 0:
                break

        else:
            mind = min(mind, a2 - a1)

print(mind)

#4 способ
mind = 10 ** 10
for a1 in range(20, 120):
    for a2 in range(a1+1, 120):
        kx = 0
        for x in range(20, 120):
            if f(a1, a2, x):
                kx += 1
        if kx == (120 - 20):
            mind = min(mind, a2 - a1)

print(mind, "долгий")

