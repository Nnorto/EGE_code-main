from itertools import *

alf = 'eloprst'
index = 0
count = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    index += 1
    if s[-1] in 'eo':
        s = s.replace('l', '*').replace('p', '*') \
            .replace('r', '*').replace('s', '*') \
            .replace('t', '*')
        if s.count('*') <= 3 and index % 2 == 1:
            count += 1
print(count)

