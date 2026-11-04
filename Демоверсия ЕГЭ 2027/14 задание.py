### 1 прототип
from string import printable
alf = printable[:22]

for x in alf:
    t1 = int(f'27{x}98876', 22)
    t2 = int(f'26{x}51', 22)
    t3 = int(f'711{x}5', 22)
    s = t1 + t2 + t3
    if s % 21 == 0:
        print(s // 21)
        break
# Ответ: 276296118

### 2 прототип
n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025
cnt = 0
while n > 0:
    if n % 25 == 0:
        cnt += 1
    n //= 25
print(cnt)
# Ответ: 10

### 3 прототип

for x in range(1, 2030+1):
    n = 7**170 + 7**100 - x
    cnt = 0
    while n > 0:
        if n % 7 == 0:
            cnt += 1
        n //= 7
    if cnt == 71:
        print(x)
# Ответ: 2029