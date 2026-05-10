s = open('files/24_23206.txt').readline()
m = 0
c = ''
for r in range(len(s)):
    c += s[r]
    if c[-1] in '02468':
        c = c[-1]
    if c.count('S') == 35:
        m = max(m, len(c))
print(m)