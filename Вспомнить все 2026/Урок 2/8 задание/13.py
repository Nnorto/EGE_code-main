from itertools import *
alf = '01234567'
cnt = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if s[0] in '1357':
            if s.count('7') <= 2:
                if s[-1] in '26':
                    cnt += 1
print(cnt)