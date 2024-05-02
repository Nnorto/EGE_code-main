s = open('24 файл').readline()
s = s.split('X')
r = 0
l = 0
t2 = 2
c2 = 0
maxk = 0
for r in range(len(s)):
    if s[r] == 'X':
        c2 += 1
    while c2 > t2:
        tk = r - l + 1
        maxk = max(maxk, tk)
        if s[l] == 'X':
            c2 -= 1
        l += 1

print(maxk)