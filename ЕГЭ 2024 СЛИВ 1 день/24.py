s = open('24 пример файла').readline()
print(len(s))
s = s.replace("CD", "*")
s = s.replace("CD", "*")
s = s.split("*")
print(s)
maxk = 0
k = 2
for i in range(len(s) - k):
    tk = k * 2
    for j in range(i, i + k + 1):
        tk += len(s[j])
    maxk = max(maxk, tk)

print(maxk)
