f = open('9.txt')
c = 0
for s in f:
    a = list(map(int, s.split()))
    count = [a.count(x) for x in a]
    sr_all = sum(a)/len(a)
    rep = [x for x in a if a.count(x) == 2]
    sr_rep = sum(rep) / 4  # 4 - количество повторяющихся чисел
    if count.count(2) == 4 and count.count(1) == 3:
        if sr_rep > sr_all:
            c += 1
print(c)