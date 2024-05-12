def f(x, a1, a2):
    return (170 <= x <= 580) <= (((not(a1<=x<=a2)) and not(290<=x<=810)) <= (not(170<= x <= 580)))

maxd = 10**10
for a1 in range(120, 850):
    for a2 in range(a1 + 1, 850):
        for x in range(120, 850):
            if f(x, a1, a2) == 0:
                break
        else:
            maxd = min(maxd, a2 - a1)

print(maxd, maxd/10)


maxd = 10**10
for a1 in range(120, 850):
    for a2 in range(a1 + 1, 850):
        if all(f(x, a1, a2) for x in range(120, 850)):
            maxd = min(maxd, a2-a1)
print(maxd, maxd/10)