def f(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


def sm(s):
    summa = 0
    for x in s:
        summa += int(x)
    return summa

res = []
for n in range(1, 1000):
    n3 = f(n)
    if n % 3 == 0:
        n3 += n3[-2:]
    else:
        # как найти сумму цифр трочиной записи
        sposob1 = n3.count('1') + n3.count('2') * 2
        sposob2 = sum(map(int, n3))
        sposob3 = sum([int(x) for x in n3])
        sposob4 = sm(n3)

        summa = sposob3 * 2
        n3 += f(summa)

    r = int(n3, 3)
    if r % 2 != 0 and r > 520:
        res.append(r)

print(min(res))