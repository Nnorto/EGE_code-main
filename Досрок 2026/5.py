res = []
for n in range(1, 1000):
    n2 = f'{n:b}'
    n2 += str(n2.count('1') % 2)
    n2 += str(n2.count('1') % 2)
    r = int(n2, 2)
    if r > 253:
        res.append(n)
print(min(res))