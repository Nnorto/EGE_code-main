from fnmatch import *

for n in range(1991, 10**8):
    if fnmatch(str(n), '2*1?71'):
        print(n, n // 1991)