def f(x, a1, a2):
    q = 17 <= x <= 58
    p = 29 <= x <= 81
    a = a1 <= x <= a2
    return (q) <= (((not (a)) and (not (p))) <= (not (q)))

res = []
d = [el for x in [17, 58, 29, 81] for el in [x-0.1, x, x+0.1]]
for a1 in d:
    for a2 in d:
        if a2 > a1 and all(f(x, a1, a2) for x in d):
            res.append(a2-a1)

print(max(res))