from itertools import *

count = 0
for x in product("комбайн", repeat=7):
    s = ''.join(x)
    if s[0] != 'й' and 'ай' not in s:
        if s.count('к') == 1 and s.count('о') == 1 and s.count('м') == 1 and s.count('б') == 1 \
                and s.count('а') == 1 and s.count('й') == 1 and s.count('н') == 1:
            count += 1


print(count)

#или

from itertools import *

s_count = 0
for x in product("комбайн", repeat=7):
    ss = ''.join(x)
    if ss[0] != 'й' and 'ай' not in ss:
        if len(set(ss)) == len(ss):
            s_count += 1


print(s_count)

#или

from itertools import product, permutations
alf = 'kombain'
c = 0
for x in permutations(alf, 7):
    sss = ''.join(x)
    if sss[0] != 'i' and 'ai' not in sss:
        c += 1
print(c)
