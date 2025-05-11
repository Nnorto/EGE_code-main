for x in range(16):
    t1 = int(f'10BAD',16) + x*16**3
    t2 = int(f'2C0FE',16) + x*16**2
    s = t1 + t2
    if s % 15 == 0:
        print(s//15)
        break