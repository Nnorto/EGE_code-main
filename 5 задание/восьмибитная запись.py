for n in range(0, 255 + 1):
    n2 = bin(n)[2:].zfill(8)
    s = ''
    for x in n2:
        if x == '0':
            s += '1'
        else:
            s += '0'
    r = int(s, 2)
    if (r - n) == 113:
        print(n)
