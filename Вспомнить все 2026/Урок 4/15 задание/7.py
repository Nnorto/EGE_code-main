def f(x, a1, a2):
    D = 17 <= x <= 58
    C = 29 <= x <= 80
    A = a1 <= x <= a2
    return (D) <= (((not (C)) and (not (A))) <= (not (D)))

# d = [16.9, 17, 17.1, 28.9, 29, 29.1, 57.9, 58, 58.1, 79.9, 80, 80.1]
d = [p for x in [17, 29, 58, 80] for p in [x - 0.1, x, x + 0.1]]
print(d)
res = []
for a1 in d:
    for a2 in d:
        if a2 > a1 and all(f(x, a1, a2) for x in d):
            res.append(a2-a1)

print(round(min(res)))