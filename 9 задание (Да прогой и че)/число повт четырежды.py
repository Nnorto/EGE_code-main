f = open('9.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    b = [a.count(x) for x in a]
    if b.count(4) == 4 and b.count(1) == 3:
        srall = sum(a)/7
        np = [x for x in a if a.count(x) == 1]
        sr = sum(np)/len(np)
        if sr < srall:
            k += 1
print(k)