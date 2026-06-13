from itertools import *
alf = '01234567'
cnt = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if s.count('4') == 2:
            for x in '1357': s = s.replace(x, '*')
            if '*4' not in s and '4*' not in s:
                cnt += 1
print(cnt)