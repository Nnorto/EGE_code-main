from itertools import *

alf = sorted('сорняк')
pn = 0
for x in product(alf, repeat=6):
    s = ''.join(x)
    pn += 1
    if s.count('к') <= 3 and s.count('я') == 2:
        print(pn, s)
        break