f = open('26_ЕГЭ 2026 день 1.txt')
k = int(f.readline())
n = int(f.readline())

sp = [0]*k
pos = []
for s in f:
    nach, end = [int(x) for x in s.split()]
    pos.append([nach, end])
pos.sort()
cnt = 0
last = 0
for nach, end in pos:
    for i in range(len(sp)):
        if sp[i] < nach:
            sp[i] = end
            cnt += 1
            last = i + 1
            break
print(cnt, last)