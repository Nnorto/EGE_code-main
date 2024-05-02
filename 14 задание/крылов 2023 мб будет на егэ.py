""" 1 способ """
for x in range(26):
    for y in range(26):
        t1 = int('13005', 26) + y * 26 ** 2 + x * 26
        t2 = int('24013', 26) + y * 26 ** 2
        s = t1 + t2
        if s % 8 != 0:
            break
    else:
        r1 = int('13005', 26) + 2 * 26 ** 2 + x * 26
        r2 = int('24013', 26) + 2 * 26 ** 2
        summa = r1 + r2
        print(summa // 8)
        break

print("=" * 5)



""" 2 способ """
def ss(x, y):
    t1 = int('13005', 26) + y * 26 ** 2 + x * 26
    t2 = int('24013', 26) + y * 26 ** 2
    return t1 + t2


for x in range(26):
    if all(ss(x, y) % 8 == 0 for y in range(26)):
        print(ss(x, 2) // 8)
        break

print("=" * 5)



"""3 способ"""
for x in range(26):
    k = 0
    for y in range(26):
        n1 = int("13" + "00" + "5", 26) + x * 26 + y * 26 ** 2
        n2 = int("24013", 26) + y * 26 ** 2
        r = n1 + n2
        if r % 8 == 0:
            k += 1
        if k >= 26:
            print((int("13" + "00" + "5", 26) + x * 26 + 2 * 26 ** 2 + int("24013", 26) + 2 * 26 ** 2) // 8)

