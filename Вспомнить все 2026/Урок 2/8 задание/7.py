from itertools import *
alf = 'abcx'
cnt = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s.count('x') == 0:
        cnt += 1
    if s.count('x') == 1 and s[-1] == 'x':
        cnt += 1

print(cnt)