s = open('../file24/24_23osn1.txt').readline()
md = 0
c = ''
for r in range(len(s)):
    c += s[r]
    while c.count('A') > 120:
        c = c[1:]
    md = max(len(c), md)

print(md)

