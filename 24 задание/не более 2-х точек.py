s = open('24 файл').readline()
s = s.split('.')
maxk = 0
for i in range(len(s) - 2):
    tk = len(s[i]) + len(s[i+1]) + len(s[i + 2]) +1
    maxk = max(maxk, tk)
print(maxk)
