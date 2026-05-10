s = open('files/24_13100.txt').readline()
c = ''
m = 0
for r in range(len(s)):
    c += s[r]
    while c.count('C') > 2 or c.count('D') > 2:
        c = c[1:]
    m = max(m, len(c))

print(m)