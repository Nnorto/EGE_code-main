for n in range(1, 1000):
    n2 = f'{n:b}'
    if len(n2) % 2 == 0:
        lev = n2[:len(n2)//2]
        prav = n2[len(n2)//2:]
        n2 = lev + '1' + prav
    r = int(n2, 2)
    if r >= 26:
        print(n)
        break