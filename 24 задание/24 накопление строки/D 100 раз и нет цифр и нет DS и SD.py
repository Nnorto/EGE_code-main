s = open('files/24-293.txt').readline()
for x in '1234567890':
    s = s.replace(x, '0')
c = ''
m = 0

for r in range(len(s)):
    c += s[r]
    while c.count('D') > 100 or '0' in c or 'DS' in c or 'SD' in c:
       c = c[1:]
    m = max(m, len(c))

print(m)