for x in range(1, 1000):
    n = 9**1942 + 9 * 6**971 + 214 - x
    k2, k8 = 0, 0
    while n > 0:
        if n % 9 == 2:
            k2 += 1
        if n % 9 == 8:
            k8 += 1
        n //= 9
    if abs(k2 - k8) == 471:
        print(x)
        break