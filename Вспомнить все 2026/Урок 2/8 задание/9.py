from itertools import *
alf = '01234567'
cnt = 0
for x in product(alf, repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if len(set(s)) == 5:
            for x in '0246':
                s = s.replace(x, '!')
            for x in '1357':
                s = s.replace(x, '*')
            if '!!' not in s and '**' not in s:
                cnt += 1

print(cnt)