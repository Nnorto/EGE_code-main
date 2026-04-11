from itertools import *

alf = sorted('апрель')
pn = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    pn += 1
    if pn % 2 == 0 and s[0] not in 'ьр' and s.count('л') >= 2:
        print(pn, s)