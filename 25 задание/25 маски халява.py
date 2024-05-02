from fnmatch import *
for i in range(0, 10**8, 1991):
    s = str(i)
    if fnmatch(s, '2*1?71'):
        print(i, i // 1991)