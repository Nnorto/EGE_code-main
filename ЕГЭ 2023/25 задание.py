from fnmatch import *
for x in range(0, 10**8, 1991):
    if fnmatch(str(x), '2*1?71'):
        print(x, x // 1991)