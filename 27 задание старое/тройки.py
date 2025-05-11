f = open('27 файлы/27-29b.txt')
n = int(f.readline())
k = 7
s = [0]* k
for x in f:
    pair = list(map(int, x.split()))
    vs = [x + y for x in s for y in pair]

    proms = [0]*k
    for i in vs:
        proms[i % k] = max(proms[i % k], i)

    s = [x for x in proms if x != 0]
print(s[0])

f = open('27 файлы/27-29b.txt')
n = int(f.readline())
k = 7
s = [0]*k
a, b, c = map(int, f.readline().split())
allsum = a + b + c
a, b, c= max(a, b, c), allsum - (min(a, b, c) + max(a, b, c)), min(a, b, c)
s[c % k] = c
s[b % k] = b
s[a % k] = a
for x in f:
    a, b, c = map(int, x.split())
    vs = []
    for i in s:
        if i != 0:
            vs.append(a + i)
            vs.append(b + i)
            vs.append(c + i)
    proms = [0]*k
    for i in vs:
        proms[i % k] = max(proms[i % k], i)
    s = proms.copy()

print(s[0])