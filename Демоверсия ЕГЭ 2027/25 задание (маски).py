from fnmatch import fnmatch
for n in range(1917, 10**10, 1917):
    if fnmatch(str(n), '3?12?14*5'):
        print(n, n // 1917)