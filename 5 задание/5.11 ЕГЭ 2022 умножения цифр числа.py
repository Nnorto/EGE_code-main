for n in range(100, 1000):
    n1 = (n // 100) * ((n % 100) // 10)
    n2 = ((n % 100) // 10) * (n % 10)
    s1 = str(n1)
    s2 = str(n2)
    r = ''
    if n1 > n2:
        r = s1 + s2
    else:
        r = s2 + s1
    if int(r) == 205:
        print(n)
        break
