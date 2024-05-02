def dell(x, a):
    if x % a == 0:
        return 1
    return 0


def f(a, x):
    return dell(x, a) or ((40 <= x <= 50) <= (not dell(x, 12)))


# 1 способ

for a in reversed(range(1, 500)):
    if all(f(a, x) for x in range(1, 500)):
        print(a)
        break

# 2 способ
for a in reversed(range(1, 500)):
    flag = True
    for x in range(1, 500):
        if (dell(x, a) or ((40 <= x <= 50) <= (not dell(x, 12)))) == 0:
            flag = False
    if flag:
        print(a)
        break

# 3 способ

for a in reversed(range(1, 500)):
    for x in range(1, 500):
        if (dell(x, a) or ((40 <= x <= 50) <= (not dell(x, 12)))) == 0:
            break

    else:
        print(a)
        break

# 4 способ
for a in reversed(range(1, 500)):
    kx = 0
    for x in range(1, 500):
        if (dell(x, a) or ((40 <= x <= 50) <= (not dell(x, 12)))) == 1:
            kx += 1
    if kx == (500 - 1):
        print(a, "долгий")
        break


