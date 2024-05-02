from fnmatch import *

for i in range(0, 10**8, 2024):
    s = str(i)
    if fnmatch(s, '1?4*78*') and sum(list(map(int, s))) < 35:
        print(i)