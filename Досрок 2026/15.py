def f(x, a1, a2):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not (A))) <= (not (P)))

res = []
d = [x for p in [25, 64, 40, 115] for x in [p - 0.1, p, p + 0.1]]
for a1 in d:
    for a2 in d:
        if a2 > a1 and all(f(x, a1, a2) for x in d):
            res.append(a2-a1)

print(round(min(res)))
