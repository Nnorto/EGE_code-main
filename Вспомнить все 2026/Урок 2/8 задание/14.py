from itertools import *
alf = '01234567'
cnt = 0
for x in product(alf, repeat=4):
    s = ''.join(x)
    if s[0] != '0':
        for x in alf:
            if x + x in s and s.count(x) == 2:
                cnt += 1
                break
print(cnt)

