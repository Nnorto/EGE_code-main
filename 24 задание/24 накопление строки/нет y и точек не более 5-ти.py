s = open('files/24_2577.txt').readline()

c = ''
m = 0

for r in range(len(s)):
    c += s[r]
    while c.count('.') > 5 or 'Y' in c:
        c = c[1:]
    m = max(m, len(c))

print(m)