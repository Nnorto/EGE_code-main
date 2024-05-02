for a in range(500):
    count = 0
    for x in range(1000):
        for y in range(1000):
            if ((3*x + y > a) and (y < x) and (x < 30)) == 0:
                count += 1
    if count == 1_000_000:
        print(a)
        exit()
