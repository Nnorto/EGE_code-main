f = open('Файлы/26_22606.txt')
count_gruz, max_raz, max_massa = map(int, f.readline().split())

a = [int(x) for x in f]
a.sort()
trums = []

trum = [0]
for el in a:
    if el - min(trum) <= max_raz and el + sum(trum) <= max_massa:
        if trum.count(0) == 1:
            trum.remove(0)
        trum.append(el)
    else:
        trums.append(trum)
        trum = [el]
trums.append(trum)
print(len(trums), len(min(trums)))