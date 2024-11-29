from itertools import *
alf = '012345678'
c = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s.count('6') == 1:
        s = s.replace('2', '*').replace('3', '*').replace('4', '*').replace('5', '*')
        if '*6' not in s and '6*' not in s:
            c += 1
print(c)