for n in range(4, 10000):
    s = '7' + n*'8'
    while '78' in s or '688' in s or '8888' in s:
        if '78' in s:
            s = s.replace('78', '8', 1)
        if '688' in s:
            s = s.replace('688', '87', 1)
        if '8888' in s:
            s = s.replace('8888', '6', 1)
    sm = sum(map(int, s))
    if sm == 61:
        print(n)
        break