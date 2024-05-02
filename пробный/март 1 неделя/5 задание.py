for n in range(1002, 10000):
    if len(set(str(n))) == 4:
        a = list(map(int, str(n)))
        a.sort()
        n1 = a[0] + a[3]
        n2 = a[1] * a[2]
        r = int(str(n2) + str(n1))
        if r > 85:
            print(n, r)
            break




