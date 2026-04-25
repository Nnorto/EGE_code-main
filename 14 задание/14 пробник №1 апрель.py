for x in range(16, 21):
    for y in range(x):
        t1 = int('13F10', x) + y * x ** 0
        t2 = int('15050', 21) + x * 21 ** 2 + y * 21 ** 0
        s = t1+t2
        if s % 32 == 0:
            print(s // 32)