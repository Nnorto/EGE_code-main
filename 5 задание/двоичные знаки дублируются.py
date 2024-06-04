for n in range(1, 1000):
    n2 = bin(n)[2:]
    s = ''
    for x in n2:
        if x == '0':
            s += '00'
        else:
            s += '11'

    r = int(s, 2)
    if r > 63:
        print(n)
        break

