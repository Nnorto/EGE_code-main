from itertools import *
count = 0
for x in product("ABC", "ABC", "ABC", "ABC", "ABCX"):
    s = ''.join(x)
    count += 1

print(count)


# или

f_count = 0
for x in product("ABCX", repeat=5):
    f = ''.join(x)
    if ('X' not in f) or ((f.count('X') == 1) and f[-1] == 'X'):
        f_count += 1

print(f_count)
