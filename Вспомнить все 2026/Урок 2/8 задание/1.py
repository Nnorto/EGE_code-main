from itertools import *

alf = sorted('атом')
pn = 0
for x in product(alf, repeat=4):
    s = ''.join(x)
    pn += 1
    if s[0] == 'о':
        print(pn, s)