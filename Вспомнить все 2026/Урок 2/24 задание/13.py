s = open('../file24/24_23osn1.txt').readline()
md = 10**10
c = ''
for r in range(len(s)):
    c += s[r]
    while c.count('A') == 120:
        md = min(md, len(c))
        c = c[1:]
print(md)