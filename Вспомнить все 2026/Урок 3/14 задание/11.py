mcnt0 = 0
res = 0
for x in range(1, 10000+1):
    n = 25**100 - x
    cnt = 0
    while n > 0:
        if n % 25 == 0:
            cnt += 1
        n //= 25
    if cnt >= mcnt0:
        mcnt0 = cnt
        res = x
print(res)
