s = open('files/24_28765.txt').readline()

c = ''
kbc = 0
m = 0
ln = len(s)
for r in range(len(s)):
    c += s[r]
    if c[-2:] == 'BC': kbc += 1
    while kbc > 180:
        if c[:2] == 'BC': kbc -= 1
        c = c[1:]
    m = max(m, len(c))
    if r % 100_000 == 0:
        print(r, ln, m)
print(m)