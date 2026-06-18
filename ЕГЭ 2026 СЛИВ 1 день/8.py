from itertools import *
alf = '012345678'
cnt = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if s.count('3') == 2:
            for x in '157':
                s = s.replace(x, '*')
            if '*3' not in s and '3*' not in s and '33' not in s:
                cnt += 1
print(cnt)