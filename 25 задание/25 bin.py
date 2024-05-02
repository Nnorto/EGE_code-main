import fnmatch
for i in range(0, 10**10, 3123):
    s = str(i)
    if fnmatch.fnmatch(s, '3?1*57'):
        n2 = bin(i)
        if n2.count("1") < 11:
            print(s)