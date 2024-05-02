from fnmatch import *
def prime(n):
    for d in range(2, int(n ** 0.5) +1):
        if n % d == 0:
            return False
    return True
def mapsum(n):
    return sum(list(map(int, str(n))))

for i in range(0, 10**10, 1234):
    s = str(i)
    if fnmatch(s, '14?127*0') and prime(mapsum(i)):
        print(i, i // 1234)
