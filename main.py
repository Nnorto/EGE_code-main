from itertools import *

alf = "кума"
c = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s[0] not in 'уа' and s[-1] in 'уа':
        c += 1
print(c)


alf = "кума"
num = 0
for x1 in "км":
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in 'уа':
                    s = x1 + x2 + x3 +x4 + x5
                    num += 1
print(num)

