s = open('24_23osn1.txt').readline()
m = 10**10
c = ''
for r in range(len(s)):
    c += s[r]
    while c.count('A') >= 120:
        m = min(m, len(c))
        c = c[1:]


print(m)