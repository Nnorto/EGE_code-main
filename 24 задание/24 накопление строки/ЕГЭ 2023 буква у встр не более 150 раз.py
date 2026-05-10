s = open('files/24-263.txt').readline()
c = ''
m = 0

for r in range(len(s)):
    c += s[r]
    while c.count('Y') > 150:
        c = c[1:]

    m = max(m, len(c))

print(m)