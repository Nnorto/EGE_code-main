s = open('../file24/24_23762.txt').readline()

md = 0

c = ''
for r in range(len(s)):
    c += s[r]
    while c.count('Y') > 80:
        c = c[1:]
    if c.count('Y') == 80 and c.count('2025') >= 90:
        md = max(md, len(c))

print(md)
