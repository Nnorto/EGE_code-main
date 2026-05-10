s = open('files/24_28943.txt').read()
for x in 'AEIOUY':
    s = s.replace(x, 'A')

c = ''
m = 10**10
for r in range(len(s)):
    c += s[r]
    if c[-1] == 'A':
        while c.count('20') >= 26:
            if c.count('20') == 26:
                m = min(m, len(c))
            c = c[1:]
        c = ''
print(m)