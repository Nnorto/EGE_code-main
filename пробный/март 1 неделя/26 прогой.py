f = open('26.txt')
count_zad = int(f.readline())
comp = []  # тип компетитонос ака  соревнования
ych = []
id = []
for i in range(count_zad):
    date, num_ych, zad = f.readline().split()
    comp.append([num_ych, int(zad), date])
    ych.append(int(num_ych))
    id.append(num_ych)
count_ych = len(list(set(ych)))
comp.sort()

# в этом массиве количество номер участника и дата последнего задания
max_count = -1
max_ych = []
for i in range(len(id)):
    count = 0
    for j in range(len(id)):
        if id[i] == id[j]:
            count += 1
            if max_count < count:
                max_count = count
        if count == 15:
            max_ych.append(id[i])
max_ych = list(set(max_ych))  # ['4041', '5110', '8203', '1871', '7905', '5823']
s = ''

for i in range(len(max_ych)):
    s += max_ych[i]

"""
# так мы ручками узнаем кто из этих ребят решил все задания первым
# ['4041', '5110', '8203', '1871', '7905', '5823']
for q in range(len(comp)):
    if comp[q][0] in s:
        print(comp[q][2][8:], comp[q][0]) 
"""

print(f' Ответ максимум заданий: {max_count}, номер участника: 4041')




