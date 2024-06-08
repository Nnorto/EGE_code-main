for a in range(1, 500):
    f = 1
    for x in range(1, 500):
        if ((x % a == 0) or ((70<=x<=90) <= (x % 27 != 0))) == 0:
            f = 0
            break

    if f:
        print(a)
