from itertools import *
alf = 'avnrbR'
count = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    count += 1
    if s[0] != 'R' and s.count('b') <= 1 and 'RR' not in s:
        print(count)