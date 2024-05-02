# нужно решать это задание исключительно увеличив все свои числа на 10
# иначе питон не будет включать дробные числа (а они тут есть!)
# print(mind/10) - нужна для того чтобы ты увидел что в ответе есть дробная часть значит надо ее округлить
def f(a1, a2, x):
    return (170 <= x <= 580) <= ((not(a1 <= x <= a2) and not(290 <= x <= 810)) <= (not (170 <= x <= 580)))


# 1 способ
mind = 10 ** 10
for a1 in range(100, 900):
    for a2 in range(a1+1, 900):
        if all(f(a1, a2, x) for x in range(100, 900)):
            mind = min(mind, a2 - a1)

print(mind/10)

# 2 способ
mind = 10 ** 10
for a1 in range(150, 900):
    for a2 in range(a1+1, 900):
        flag = True
        for x in range(150, 900):
            if f(a1, a2, x) == 0:
                flag = False
                break

        if flag:
            mind = min(mind, a2 - a1)

print(mind/10)

# 3 способ
mind = 10 ** 10
for a1 in range(150, 900):
    for a2 in range(a1+1, 900):
        kx = 0
        for x in range(150, 900):
            if f(a1, a2, x):
                kx += 1
        if kx == (900 - 150):
            mind = min(mind, a2 - a1)

print(mind/10)

#4 способ
mind = 10 ** 10
for a1 in range(150, 900):
    for a2 in range(a1+1, 900):
        for x in range(150, 900):
            if f(a1, a2, x) == 0:
                break

        else:
            mind = min(mind, a2 - a1)

print(mind/10)
