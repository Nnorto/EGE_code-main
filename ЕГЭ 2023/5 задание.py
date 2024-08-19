for n in range(2, 10000):
    n2 = bin(n)[2:]
    if n % 3 == 0:
        n2 = n2 + n2[-3:]
    else:
        ost = bin(3 * (n % 3))[2:]
        n2 += ost

    R = int(n2, 2)
    if R <= 138:
        print(R)
