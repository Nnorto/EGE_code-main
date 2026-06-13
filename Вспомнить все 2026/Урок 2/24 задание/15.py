s = open('../file24/24var04.txt').readline()
md = 0
c = ''
for r in range(len(s)):
    c += s[r]
    while c.count('A') > 500 or 'E' in c:
        c = c[1:]
    md = max(md, len(c))
print(md)