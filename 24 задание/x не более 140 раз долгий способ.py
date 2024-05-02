s = open('24 файл').readline()
s = s.split('X')
maxk = 0
k = 2
for i in range(len(s) - k):
    tk = k
    for j in range(i, i + k + 1):
        tk += len(s[j])
    maxk = max(maxk, tk)
print(maxk)
