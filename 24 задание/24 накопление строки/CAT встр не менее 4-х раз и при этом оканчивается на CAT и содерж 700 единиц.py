s = open('files/24var03.txt').readline()

c = ''
m = 0
k = 0

for r in range(len(s)):
    c += s[r]
    if c[-1] == '1': k += 1

    if c[-3:] == 'CAT':
        while k > 700:
            if c[0] == '1': k -= 1
            c = c[1:]
        if c.count('CAT') >= 4 and k == 700:
            m = max(m, len(c))
    if r % 100_000 == 0:
        print(r, len(s), m)
print(m)
