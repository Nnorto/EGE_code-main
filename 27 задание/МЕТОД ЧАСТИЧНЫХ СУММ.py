f = open('27 файлы/27-B пары.txt')
n = int(f.readline())
k = 4
s = [0]* k
for x in f:
    pair = list(map(int, x.split()))
    vs = [x + y for x in s for y in pair]

    proms = [0]*k
    for i in vs:
        proms[i % k] = max(proms[i % k], i)

    s = [x for x in proms if x != 0]
print(s[0])

f = open('27 файлы/27-B пары.txt')
n = int(f.readline())
k = 4
s = [0]*k
a, b = map(int, f.readline().split())
a, b = max(a, b), min(a, b)
s[b % k] = b
s[a % k] = a
for x in f:
    a, b = map(int, x.split())
    vs = []
    for i in s:
        if i != 0:
            vs.append(a + i)
            vs.append(b + i)
    proms = [0]*k
    for i in vs:
        proms[i % k] = max(proms[i % k], i)
    s = proms.copy()

print(s[0])