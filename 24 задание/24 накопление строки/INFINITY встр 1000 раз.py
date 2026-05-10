s = open('files/24_11667.txt').readline()

c = ''
m = 0
k = 0

for r in range(len(s)):
    c += s[r]
    if c[-8:] == 'INFINITY': k += 1
    while k > 1000:
        if c[:8] == 'INFINITY': k -= 1
        c = c[1:]
    m = max(m, len(c))
    if r % 100000 == 0:
        print(r, len(s), m)
print(m)