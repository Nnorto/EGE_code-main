from itertools import *

alf = sorted('строка')
pn = 0
cnt = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    pn += 1
    if pn % 2 == 0:
        if s[0] not in 'аст' and s.count('о') == 2:
            print(pn, s)
