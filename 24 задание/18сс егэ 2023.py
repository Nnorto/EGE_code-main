import string
s = open('24 файл').readline()
alf = '0123456789'+string.ascii_uppercase[:8]
maxk = 0
tk = 0
for i in range(len(s) - 1):
    if s[i] in alf:
        tk += 1
        maxk = max(maxk, tk)

    else:
        tk = 0
print(maxk)