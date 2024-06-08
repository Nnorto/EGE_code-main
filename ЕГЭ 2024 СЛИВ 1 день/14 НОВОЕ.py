for x in range(2031):
    c = 3 ** 100 - x
    s = ""
    while c > 0:
        s = str(c % 3) + s
        c //= 3
    if s.count('0') == 2:
        print(x)
        break
