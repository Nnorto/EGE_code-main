for a in range(500):
    count = 0
    for x in range(1000):
        for y in range(1000):
            if ((x < a) <= (x ** 2 < 81)) and ((y ** 2 <= 36) <= (y <= a)):
                count += 1
    if count == 1_000_000:
        print(a)
