from itertools import *

count = 0
for x in product("катер", repeat=4):
    s = ''.join(x)
    if s.count('р') >= 2:
       count += 1

print(count)
