s = open('files/24_12476.txt').readline()
c = ''
m = 0
for r in range(len(s)):
    c += s[r]
    while c.count('RO') > 21 or 'ORO' in c or 'ROR' in c:
        c = c[1:]
    m = max(m, len(c))

print(m)