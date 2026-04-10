f = open('26var03.txt')
n, m, k = [int(x) for x in f.readline().split()]
kor = []
for s in f:
    poz = [int(x) for x in s.split()]
    kor.append(poz)
kor.sort()
poz_kor = []

for stroka, stolb in kor:
    poz_kor.append([stroka-1, stolb])

kor.sort(key=lambda x: [x[1], x[0]])

for i in range(len(kor) - 1):
    stroka1, stolb1 = kor[i]
    stroka2, stolb2 = kor[i+1]
    if stolb1 != stolb2 and stroka1 != m:
        poz_kor.append([m, stolb1])
if [m, k] not in kor:
    poz_kor.append([m, k])
ans = []
for strokat, stolbt in poz_kor:
    svo = 0
    for strokaz, stolbz in kor:
        if strokat > strokaz and stolbt == stolbz:
            svo = strokat - strokaz - 1
        elif strokat == m and stolbt == stolbz:
            svo = strokat - strokaz - 1
            break
        elif strokat < strokaz and stolbt == stolbz and svo == 0:
            svo = strokat - 1
            break
    ans.append([strokat, svo])


minstroka = 123123123
max_svo = 0
for stroka, svo in ans:
    if svo > max_svo:
        max_svo = svo
        minstroka = stroka

print(minstroka, max_svo)