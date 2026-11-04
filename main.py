def f(x, a1, a2):
    B = 32 <= x <= 425
    C = 130 <= x <= 480
    D = 290 <= x <= 575
    A = a1 <= x <= a2
    return ((C) <= ((not (D)))) and (A) and ((not (B)))

res = []
d = [p for x in [32, 425, 130, 290, 480, 575] for p in [x-0.1, x, x+0.1]]
d = [31.9, 32, 32.1, 424.9, 425, 425.1, 129.9, 130, 130.1, 289.9, 290, 290.1, 479.9, 480, 480.1, 574.9, 575, 575.1]
print(d)
for a1 in d:
    for a2 in d:
        if a2 > a1 and all(f(x, a1, a2) == 0 for x in d):
            res.append(a2-a1)
print(max(res))