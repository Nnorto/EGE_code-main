for n in range(1, 1000):
    n2 = bin(n)[2:]
    if len(n2) % 2 == 0:
        n2 = n2[:len(n2)//2] + '1' + n2[len(n2)//2:]
    r = int(n2, 2)
    if r >= 26:
        print(n)
        break