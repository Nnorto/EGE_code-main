from itertools import *

alf = "012345678"
nch = '01357'
c = 0
for x in product(alf, repeat=6):
    s = ''.join(x)
    if s[0] not in nch:

        if s[-1] not in '23':
            if s.count('1') >= 2:
                c += 1
print(c)

alf = "012345678"
nch = '01357'
c = 0
for x in product(alf, repeat=6):
    s = ''.join(x)
    if s[0] not in nch:
        s = s.replace('2', '*').replace('3', '*')
        if s[-1] != "*":
            if s.count('1') >= 2:
                c += 1
print(c)

c = 0
for x in product('2468', alf, alf, alf, alf, "0145678"):
    s = ''.join(x)
    if s.count('1') >= 2:
        c += 1
print(c)

