from itertools import *

count = 0
for x in product("012345678", repeat=5):
    s = ''.join(x)
    if s.count("6") == 1 and s[0] != "0":
        s = s.replace('2', 'r').replace('3', 'r')\
            .replace('4', 'r').replace('5', 'r')
        if 'r6' not in s and '6r' not in s:
            count += 1

print(count)