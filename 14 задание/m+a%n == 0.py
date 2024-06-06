for A in range(10000):
    for x in range(13):
        for y in range(13):
            M = int("202305", 15) + x * 15 + y * 15 ** 4
            N = int("67090", 13) + y + x * 13 ** 2
            if (M + A) % N == 0:
                print(A)
                exit()