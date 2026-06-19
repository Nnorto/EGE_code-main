def f(x, a1, a2):
    p = 3 <= x <= 18
    q = 11 <= x <= 24
    a = a1 <= x <= a2
    return ((p) and (q)) <= (a)

d = [p for x in [3, 18, 11, 24] for p in [x-0.1, x, x+0.1]]
res = []
for a1 in d:
    for a2 in d:
        if a2 > a1 and all(f(x, a1, a2) for x in d):
            res.append(a2-a1)
print(min(res))