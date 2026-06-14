for x in range(10):
    t1 = 1 * int(f'12{x}34') + 9
    t2 = 2 * int(f'1{x}234') + 1
    s = t1 + t2
    if s % 11 == 0:
        print(s // 11, x)