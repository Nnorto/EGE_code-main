s = open('24_28943.txt').read()
for x in 'AEIOUY':
    s = s.replace(x, 'A')

k20 = 26
md = 10**10
cnt20 = 0
cnta = 0
l = 0
for r in range(len(s)):
    if s[r] == 'A':
        cnta += 1
    if r >= 1 and s[r - 1] + s[r] == '20':
        cnt20 += 1
    if s[r] == 'A':
        while cnt20 >= k20:
            if cnta == 1:
                td = r - l + 1
                md = min(td, md)
            if s[l] == 'A':
                cnta -= 1
            if s[l] + s[l + 1] == '20':
                cnt20 -= 1
            l += 1

print(md)