f = open("26.txt")
n = int(f.readline())
a = list(map(int, f))
a.sort(reverse=True)
tk = a[0]
count = 1
for i in range(len(a)):
    if tk-a[i] >= 8:
        tk = a[i]
        count += 1

print(count, tk)
