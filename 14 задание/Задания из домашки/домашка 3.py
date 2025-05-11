for x in range(13):
    t1 = int(f'18604',13) + x*13
    t2 = int(f'50716',13) + x*13**3
    s = t1 + t2
    if s % 11 == 0:
        print(s//11)
        break