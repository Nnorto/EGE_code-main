f = open('файлы/9_9832-2')
sums = 0
for i in f:
    a = list(map(int, i.split()))
    a.sort()
    count_num = [] # количество чисел
    for x in a:
        count_num.append(a.count(x))

    if count_num.count(2) == 4 and (count_num[-1] != 2):
        sums += sum(a)
        break
print(sums)

f = open('9 задание (Да прогой и че)/файлы/9_9832-2')
c = 0
for z in f:
    a = list(map(int, z.split()))
    a.sort()
    b = [a.count(x) for x in a]
    if b.count(1) == 3 and b.count(2) == 4:
        if a[-1] != a[-2]:
            print(sum(a))
            break