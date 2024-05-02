for n in range(4, 10000):
    n2 = bin(n)[2:]
    if n % 3 == 0:
        n2 = n2 + n2[-3::]
    else:
        ost = (n % 3)*3
        n2 = n2 + bin(ost)[2:]

    res10 = int(n2, 2)
    if res10 < 138:
        print(res10, n)

