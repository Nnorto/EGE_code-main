from itertools import *
alf = '0123'
cnt = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if s.count('3') == 1:
            if '03' not in s and '30' not in s:
                cnt += 1
print(cnt)