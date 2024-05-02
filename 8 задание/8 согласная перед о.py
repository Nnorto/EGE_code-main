from itertools import *

count = 0
for x in product("пирог", repeat=4):
    s = ''.join(x)
    if s.count('о') <= 2 and s[0] != 'о' and 'ио' not in s and 'оо' not in s:
        count += 1


print(count)
