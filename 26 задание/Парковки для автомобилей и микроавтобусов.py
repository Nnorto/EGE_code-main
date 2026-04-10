f = open('Файлы/26stat2023apr.txt')
n, p_leg, p_abobus = [int(x) for x in f.readline().split()]
a = [-1]*p_leg
m = [-1]*p_abobus
ts = []

for s in f:
    ns = s.split()
    ns[0], ns[1] = int(ns[0]), int(ns[1])
    ts.append([int(ns[0]), int(ns[1]), ns[2]])


ts.sort()
liv = 0
park = 0
for i in range(len(ts)):
    if ts[i][2] == 'B':
        for j in range(20):
            if ts[i][0] > m[j]:
                m[j] = ts[i][0] + ts[i][1] - 1
                break
        else:
            liv += 1
    else:
        for j in range(80):
            if ts[i][0] > a[j]:
                a[j] = ts[i][0] + ts[i][1] - 1
                park += 1
                break
        else:
            for j in range(20):
                if ts[i][0] > m[j]:
                    m[j] = ts[i][0] + ts[i][1] - 1
                    park += 1
                    break
            else:
                liv += 1

print(park, liv)