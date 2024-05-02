from itertools import *
count = 0
for x in product("КУМА", repeat=5):
    s = ''.join(x)
    if s[0] in 'КМ' and s[-1] in 'АУ':
        count += 1

print(count)

"""
from itertools import *
count = 0
for x in product("КМ", "КУМА", "КУМА", "КУМА", "УА"):
    s = ''.join(x)
    if s[0] in 'КМ' and s[-1] in 'АУ':
        count += 1

print(count)
"""