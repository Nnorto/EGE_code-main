for x in range(15):
    t1 = int('12305',15) + x*15
    t2 = int('10233',15) + x*15**3
    s = t1 + t2
    if s % 14 == 0:
        print(s//14)
        break