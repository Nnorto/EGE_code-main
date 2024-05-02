f = open('27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 94
mins = 10**10
minost = [10**10] * k
for i in a:
    ost = i % k
    ostnap = (k-ost) % k
    mins = min(mins, minost[ostnap] + i)
    minost[ost] = min(minost[ost], i)

print(mins)