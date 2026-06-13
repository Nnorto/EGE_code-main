from itertools import *

alf = sorted('польза')
pn = 0
for x in product(alf, repeat=6):
    s = ''.join(x)
    pn += 1
    if s.count('ь') <= 1 and s.count('а') == 1 and s.count('з') <= 2:
        print(pn, s)
        break