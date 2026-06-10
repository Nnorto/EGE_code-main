def M(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    if len(d) > 0:
        return max(d) - min(d)
    return 0

for n in range(700_000-1,699850, -1):
    m = M(n)
    if m != 0 and m % 17 == 0:
        print(n, m)