res = []
for n in range(1, 1000):
    n2 = f'{n:b}'
    if n % 2 == 0:
        n2 = '11' + n2 + '11'
    else:
        n2 = '1' + n2 + '00'
    r = int(n2, 2)
    if r > 95:
        res.append(r)

print(min(res))