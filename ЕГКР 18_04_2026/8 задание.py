from itertools import *

alf = sorted('символ')
pn = 0

for x in product(alf, repeat=5):
    s = ''.join(x)
    pn += 1

    if pn % 2 != 0:
        if s[0] not in 'ос' and s.count('в') == 1 and s.count('с') <= 1:
            print(pn, s)
