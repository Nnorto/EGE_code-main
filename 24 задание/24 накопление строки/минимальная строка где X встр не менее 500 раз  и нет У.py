s = open('files/24_11954.txt').readline()

c = ''
m = 10**10

for r in range(len(s)):
    c += s[r]
    while c.count('X') == 500 or 'Y' in c:
        if 'Y' not in c:
            m = min(m, len(c))
        c = c[1:]
    if r % 100_000 == 0:
        print(r, len(s), m)
print(m)