def f(x, a1, a2):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not (A))) <= (not (P)))

d = [p for x in [17, 29, 58, 80] for p in [x - 0.1, x, x + 0.1]]
res = []
for a1 in d:
    for a2 in d:
        if a2 > a1 and all(f(x, a1, a2) for x in d):
            res.append(a2-a1)

print(round(min(res)))