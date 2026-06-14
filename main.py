def ss(x):
    s = ''
    while x > 0:
        s = str(x % 3)
        x = x // 3
    return s[::-1]


otv = []
for n in range(10, 1000):
    n2 = ss(n)
    if n % 4 == 0:
        n2 = n2 + n2[-3:]
    else:
        n2 = '1' + n2 + '20'
    r = int(n2, 3)
    if r > 423:
        otv.append(r)
print(min(otv))
