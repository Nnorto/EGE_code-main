for n in range(1, 115):
    n2 = bin(n)[2:]
    if n2[-1] == 0:
        n2 += '00'
    else:
        n2 += '11'
    r = int(n2, 2)
    if r > 115:
        print(n)
        break

