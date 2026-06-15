a = []

for x in range(1, 1000):
    P = x in [x for x in range(2, 20 + 1, 2)]
    Q = x in [x for x in range(3, 30 + 1, 3)]
    f = ((P) <= (x in a)) or ((x not in a) <= (not Q))
    if f == 0:
        a.append(x)

print(a)