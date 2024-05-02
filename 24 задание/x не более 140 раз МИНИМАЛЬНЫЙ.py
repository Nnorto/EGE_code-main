
s = open('24 пример файла').readline()
s = s.split('X')
dx = 3
tk = dx
for i in range(1, dx):
    tk += len(s[i])
mink = tk
for i in range(2, len(s) - dx):
    tk = tk - len(s[i - 1]) + len(s[i + dx - 2])
    mink = min(mink, tk)
print(mink)
