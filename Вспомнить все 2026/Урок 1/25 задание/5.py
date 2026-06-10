def M(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    if len(d) > 0:
        return max(d) + min(d)
    return 0

for n in range(900_001, 900_101):
    m = M(n)
    if m and m % 10 == 4:
        print(n, m)