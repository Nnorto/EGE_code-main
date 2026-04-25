s = open('Файлы/24_23762.txt').read()
ky = 80
l = 0
md = 0
cnty = 0
cnt25 = 0

for r in range(len(s)):
    if s[r] == 'Y':
        cnty += 1
    if r >= 3 and s[r-3] + s[r-2] + s[r-1] + s[r] == '2025':
        cnt25 += 1
    while cnty > ky:
        if s[l] == 'Y':
            cnty -= 1
        if s[l] + s[l+1]+s[l+2] + s[l+3] == '2025':
            cnt25 -= 1
        l += 1
    if cnty == 80 and cnt25 >= 90:
        td = r - l + 1
        md = max(td, md)
print(md)

# ans 2981