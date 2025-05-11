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
a, b = min(a, b), max(a, b)  # разбираем отдельно первую строчку
s[a % k] = a  # исключаем ситуацию чтобы записаласть строго максимальная сумма
s[b % k] = b
for i in range(1, n):
    a, b = map(int, f.readline().split())
    vs = []  # создаем возможные суммы
    for x in s:
        if x != 0:
            vs.append(x + a)
            vs.append(x + b)
    sp = [0] * 4  # предварительные суммы с тек шага
    for x in vs:
        sp[x % k] = max(sp[x % k], x) # максимальные суммы с опред остатком

    s = sp.copy()  # предварительные суммы (итоговые) копируем в главный массив

print(max(s[1:4]))
print(s[0], 'answ')