from itertools import *

alf = '012345678'
count = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if s.count('5') == 1:
            s = s.replace('11', '*').replace('22', '*').replace('33', '*') \
                .replace('44', '*').replace('55', '*').replace('66', '*') \
                .replace('77', '*').replace('88', '*').replace('00', '*')
            if s.count('*') == 0:
                count += 1
print(count)
