for x in range(1, 3000+1):
    n = 9**150 + 9**30 - x
    k0 = 0
    while n > 0:
        if n % 9 == 0:
            k0 += 1
        n //= 9
    if k0 == 122:
        print(x)
        break