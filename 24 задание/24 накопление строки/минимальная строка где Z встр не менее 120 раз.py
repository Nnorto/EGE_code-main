s = open('files/24-263.txt').readline()

c = ''
m = 10**10

for r in range(len(s)):
    c += s[r]
    while c.count('Z') == 120:
        m = min(m, len(c))
        c = c[1:]

print(m)