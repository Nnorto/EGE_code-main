s = open('../file24/24var04.txt').readline()
m = 0
c = ''
for r in range(len(s)):
    c += s[r]
    while c.count('A') > 500 or 'E' in c:
        c = c[1:]
    m = max(m, len(c))


print(m)