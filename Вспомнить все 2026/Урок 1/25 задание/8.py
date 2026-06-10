from fnmatch import *

for n in range(2025, 10**10, 2025):
    for x in range(1, 3+1):
        s = '?'*x
        if fnmatch(str(n), f'10{s}0'):
                print(n)

print('!!!!!!!!')

from re import *
for n in range(2025, 10**8, 2025):
    if fullmatch(r'10[0-9]{1,3}0', str(n)):
        print(n)


print('!!!!!!!!')

for n in range(2025, 10**10, 2025):
    s = [str(x) for x in range(0, 1000)] + [str(x).zfill(3) for x in range(0, 100)]
    for x in s:
        if fnmatch(str(n), f'10{x}0'):
            print(n)

