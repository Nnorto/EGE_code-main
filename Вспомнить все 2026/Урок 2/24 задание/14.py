s = open('../file24/24var07.txt').readline()
md = 0
c = ''
for r in range(len(s)):
    c += s[r]
    while c.count('AB') > 21:
        c = c[1:]
    md = max(md, len(c))
print(md)