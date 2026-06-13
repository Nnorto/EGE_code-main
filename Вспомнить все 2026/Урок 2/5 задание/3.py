for n in range(1, 1000):
    n2 = f'{n:b}'
    if n % 2 == 0:
        n2 += '0'
    else:
        n2 += '1'
    if n2.count('1') % 3 == 0:
        n2 = '11' + n2[2:]
    else:
        n2 = '10' + n2[2:]

    r = int(n2, 2)
    if r <= 37:
        print(n)
