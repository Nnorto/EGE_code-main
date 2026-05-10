s = open('files/24_23762.txt').readline()

c = ''
m = 0

for r in range(len(s)):
    c += s[r]
    while c.count('Y') > 80:
        c = c[1:]
    if c.count('2025') >= 90 and c.count('Y') == 80:
        m = max(m, len(c))
    if r % 100000 == 0:
        print(r, len(s), m)
print(m)