maxs = 0
for n in range(4, 10000):
    s = '4' + n*'7'
    while '444' in s or '777' in s:
        if '777' in s:
            s = s.replace('777', '4', 1)
        else:
            s = s.replace('444', '7', 1)
    sm = sum(map(int, s))
    maxs = max(maxs, sm)

print(maxs)