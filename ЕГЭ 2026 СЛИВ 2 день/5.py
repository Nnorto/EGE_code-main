for n in range(1, 1000):
    n2 = f'{n:b}'
    if n2.count('1') % 2 != 0:
        n2 += '01'
    else:
        n2 += '10'
    r = int(n2, 2)
    if r > 123:
        print(r)