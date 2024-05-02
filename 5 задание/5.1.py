for n in range(1, 57):
    n2 = bin(n)[2::]
    summa = n2.count('1')
    ost = summa % 2
    n2 += str(ost)
    summa = n2.count('1')
    ost = summa % 2
    n2 += str(ost)
    r = int(n2, 2)
    if r > 57:
        print(n)
        break