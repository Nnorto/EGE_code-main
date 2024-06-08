def dell(n):
    vs = []
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if d * d == n:
                vs.append(d)
            else:
                vs.append(d)
                vs.append(n//d)
    if len(vs) > 0:
        return max(vs) + min(vs)
    else:
        return 0
k = 0
for x in range(700_001, 10 ** 10):
    m = dell(x)
    if m % 10 == 4:
        print(x, m)
        k += 1
        if k == 5:
            break

