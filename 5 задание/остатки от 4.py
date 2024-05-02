for n in range(100):
    n2 = bin(n)[2:]
    n2 += bin(n % 4)[2:].zfill(2)
    r = int(n2, 2)
    if r < 100:
        print(r, n)