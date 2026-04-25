s = open('Файлы/24_droch3.txt').read()
# s = open('test.txt').read()
kx = 60
md = 0
l = 0
cnt26 = 0
cntx = 0
for r in range(len(s)):
    if s[r] == 'X':
        cntx += 1
    if r >= 3 and s[r - 3] + s[r - 2] + s[r - 1] + s[r] == '2026':
        cnt26 += 1
    while cntx > kx:
        if s[l] == 'X':
            cntx -= 1
        if s[l] + s[l + 1] + s[l + 2] + s[l + 3] == '2026':
            cnt26 -= 1
        l += 1
    if cntx == kx and cnt26 >= 75:
        td = r - l  + 1
        md = max(td, md)

print(md)
