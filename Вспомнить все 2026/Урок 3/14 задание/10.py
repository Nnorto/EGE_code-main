mcnt0 = 0
res = 0
for x in range(1, 2030 + 1):
    n = 4 ** 150 - 4 ** 100 - x
    cnt = 0
    while n > 0:
        if n % 4 == 0:
            cnt += 1
        n //= 4
    if cnt >= mcnt0:
        mcnt0 = cnt
        res = x
print(res)
