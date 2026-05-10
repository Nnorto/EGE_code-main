s = open('files/24_23206.txt').readline()
s = s[::-1]
m = 0
c = ''
for r in range(len(s)):
    c += s[r]
    if c[-1] in '02468':
        while c.count('S') > 35:
            c = c[1:]
        if c.count('S') == 35:
            m = max(m, len(c))

print(m)

s = open('files/24_23206.txt').readline()
m = 0
c = ''
for r in range(len(s)):
    c += s[r]
    while c.count('S') > 35 or (len(c) > 0  and c[0] not in '02468'):
        c = c[1:]
    if c.count('S') == 35:
        m = max(m, len(c))

print(m)