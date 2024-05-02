s = open('24 задание/Файлы/24var03.txt').readline()
dx = 500
kx = 0
l = 0
mink = 10**10
for r in range(len(s)):
    if s[r] == 'A':
        kx += 1
    while kx >= dx:
        mink = min(mink, r - l + 1)
        if s[l] == 'A':
            kx -= 1
        l += 1
print(mink)
