s = open('2024_Файлы/24.txt').readline()

s = s.replace("CD", "C*D")
s = s.split("*")

tk = 0
k = 140
for i in range(k + 1):
    tk += len(s[i])
maxk = tk
for i in range(1, len(s) - k):
    tk = tk - len(s[i-1]) + len(s[i + k])
    maxk = max(maxk, tk)
print(maxk)


s = open('2024_Файлы/24.txt').readline()

l = r = 0
dx = 140
kx = 0
maxk = 0
for r in range(len(s) - 1):
    if s[r] + s[r + 1] == 'CD':
        kx += 1
    while kx > dx:
        if s[l] + s[l + 1] == 'CD':
            kx -= 1
        l += 1
    maxk = max(maxk, r - l + 2)

print(maxk)
