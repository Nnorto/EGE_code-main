s = '1231231313131231'
print(len(s))
r = 0
l = 0
t2 = 2
c2 = 0
maxk = 0
for r in range(len(s)):
    if s[r] == '2':
        c2 += 1
    while c2 > t2:
        if s[l] == '2':
            c2 -= 1
        l += 1
    tk = r - l + 1
    maxk = max(maxk, tk)
print(maxk)