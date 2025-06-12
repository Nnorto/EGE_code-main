from itertools import *

alf = 'еиортя'
ns = 0
for x in product(alf, repeat=6):
    s = ''.join(x)
    ns += 1
    if s[0] not in 'ртя' and s.count('и') >= 2 and ns % 2 != 0:
        print(ns)
