from fnmatch import *
for i in range(1917, 10**10, 1917):
    s=str(i)
    if fnmatch(s, '3?12?14*5'):
        print(i, i // 1917)

print('***')

from re import *
for i in range(1917, 10**10, 1917):
    if fullmatch("3\d12\d14\d*5", str(i)):
        print(i, i // 1917)