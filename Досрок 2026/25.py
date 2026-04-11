def dell(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 10 == 7 and i != 7:
                d.add(i)
            if (n//i) % 10 == 7 and (n//i) != 7:
                d.add(n//i)

    if d:
        return d
    return 0


for n in range(700_001, 700_101):
    a = dell(n)
    if a:
        print(n, min(a))

# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167