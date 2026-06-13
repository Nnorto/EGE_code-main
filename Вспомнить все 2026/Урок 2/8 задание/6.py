from itertools import *
alf = '123456'
cnt = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s.count('1') == 1:
        cnt += 1
print(cnt)