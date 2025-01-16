for n in range(61, 100000):
    n2 = bin(n)[2:]

    c0 = n2.count('0')
    c1 = n2.count('1')
    if c0 == c1:
        n2 += n2[-1]
    else:
        if c0 < c1:
            n2 += '0'
        else:
            n2 += '1'

    c0 = n2.count('0')
    c1 = n2.count('1')
    if c0 == c1:
        n2 += n2[-1]
    else:
        if c0 < c1:
            n2 += '0'
        else:
            n2 += '1'

    c0 = n2.count('0')
    c1 = n2.count('1')
    if c0 == c1:
        n2 += n2[-1]
    else:
        if c0 < c1:
            n2 += '0'
        else:
            n2 += '1'

    r = int(n2, 2)
    if r % 2 == 0 and r % 4 != 0:
        print(n)
        break