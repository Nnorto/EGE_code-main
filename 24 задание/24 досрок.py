s = open('Файлы/24_28765.txt').read()
l = 0
k = 180
md, cnt = 0, 0
for r in range(1, len(s)):
    if s[r - 1] + s[r] == 'BC':
        cnt += 1
    while cnt > k:
        if s[l] + s[l + 1] == 'BC':
            cnt -= 1
        l += 1

    td = r - l + 1
    md = max(td, md)

print(md)