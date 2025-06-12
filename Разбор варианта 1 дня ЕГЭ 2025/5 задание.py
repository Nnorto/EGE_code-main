for n in range(1, 1000):
    n2 = f'{n:b}'
    if n % 3 == 0:
        n2 += n2[-3:]
    else:
        ost = (n % 3) * 3
        ost2 = f'{ost:b}'
        n2 += ost2

    r = int(n2, 2)
    if r < 130:
        print(n)