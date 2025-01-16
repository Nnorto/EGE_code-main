f = open('файлы/KIM_0015973096_9')  # файл нужен другой
count = 0
for s in f:
    a = [int(el) for el in s.split()]
    a.sort()
    b = [a.count(el) for el in a]
    if a.count(2) == 6:
        y = [el for el in a if a.count(el) == 2]
        w = [el for el in a if a.count(el) == 1]
        if (min(y) + max(y)) / 2 < w[0]:
            count += 1
print(count)
