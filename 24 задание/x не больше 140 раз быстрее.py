s = open('24 задание/Файлы/24_1.txt').readline()
s = s.split('X')
dx = 3
tk = dx
for i in range(dx+1):
    tk += len(s[i])
maxk = tk
for i in range(1, len(s) - dx):
    tk = tk - len(s[i - 1]) + len(s[i + dx])
    maxk = max(maxk, tk)
print(maxk)
