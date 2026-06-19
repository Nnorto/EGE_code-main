def dell(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    if len(d) == 4:
        return sum(d)
    return 0

for n in range(8_494_154+1, 10**10):
    s = dell(n)
    if s and str(s) == str(s)[::-1]:
        print(n, s)
