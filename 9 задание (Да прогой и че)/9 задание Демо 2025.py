f = open('файлы/9-4.txt')
count = 0
for s in f:
    a = [int(el) for el in s.split()]
    a.sort()
    b = [a.count(el) for el in a]
    if b.count(3) == 3 and b.count(1) == 3:
        r = [el for el in a if a.count(el) == 3]
        w = [el for el in a if a.count(el) == 1]
        if sum(r) ** 2 > sum(w) ** 2:
            count += 1
print(count)
