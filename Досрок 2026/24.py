s = open('24_28765.txt').read()
k = 180
l = 0
md = 0
cbc = 0
for r in range(1, len(s)):
    if s[r-1] + s[r] == 'BC':
        cbc += 1

    while cbc > k:
        if s[l] + s[l+1] == 'BC':
            cbc -= 1
        l += 1
    td = r - l + 1
    md = max(td, md)

print(md)

