from itertools import *

alf = sorted('реплика')
pn = 0
cnt = 0
for x in product(alf, repeat=6):
    s = ''.join(x)
    pn += 1
    if pn % 2 == 0:
        if s[0] != 'к' and s.count('и') >= 2:
            cnt += 1
print(cnt)