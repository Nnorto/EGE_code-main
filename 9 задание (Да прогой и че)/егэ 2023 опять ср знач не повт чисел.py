f = open('файлы/KIM_0016473286_9')
index = 0
res = 0
for i in f:
    a = list(map(int, i.split()))
    a.sort()
    count_num = []  # количество чисел
    for x in a:
        count_num.append(a.count(x))
    index += 1
    if count_num.count(2) == 2 and count_num.count(1) == 4:
        not_rep_num = [x for x in a if a.count(x) == 1]
        rep_number = (sum(a)-sum(not_rep_num))//2
        sr_rep = sum(not_rep_num)/len(not_rep_num)
        if rep_number > sr_rep:
            res = index


print(res)