s = open('../file24/24_28943.txt').readline()
md = 10**10
for x in 'AEIOUY': s = s.replace(x, 'A')
c = ''
for r in range(len(s)):
    c += s[r]
    if c[-1] == 'A':
        while c.count('20') > 26:
            c = c[1:]
            md = min(md, len(c))

print(md)