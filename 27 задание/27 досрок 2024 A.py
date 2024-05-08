f = open('27 пример')
n = int(f.readline())
a = [int(x) for x in f]
mins = 10**10
for i in range(len(a)):
    s = 0
    for j in range(len(a)):
        s += min(abs(j - i), n - abs(j-i)) * a[j]
    mins = min(mins, s)
print(mins)