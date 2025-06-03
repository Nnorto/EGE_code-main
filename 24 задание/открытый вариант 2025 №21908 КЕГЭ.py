import string
f = open("Файлы/24_21908.txt").readline()
for x in string.printable[14:].upper():
    f = f.replace(x, '*')
m = 0
for l in range(len(f)):
    for r in range(l+m, len(f)):
        s = f[l:r+1]
        if '*' not in s and int(s, 14) % 2 == 0 and s[0] != '0':
            m = max(m, len(s))
        else:
            break
print(m)