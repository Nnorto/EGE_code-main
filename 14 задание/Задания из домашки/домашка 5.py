for x in range(17):
    t1 = int('97590',17) + x*17**0
    t2 = int('30108',17) + x*17**3
    s = t1 + t2
    if s % 11 == 0:
        print(s//11)
        break