s = open('files/24-309.txt').readline()

c = ''
m = 0

for r in range(len(s)):
    c += s[r]
    while c.count('FSRQ') > 80:
        c = c[1:]
    if c.count('FSRQ') == 80:
        m = max(m, len(c))

print(m)