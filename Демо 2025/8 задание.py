from itertools import *
alf = '0123456789ab'
c = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s.count('7') == 1:
        s = s.replace('9', '*')
        s = s.replace('a', '*')
        s = s.replace('b', '*')
        if s.count('*') <= 3:
            c += 1

print(c)
