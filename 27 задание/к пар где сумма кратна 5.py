f = open('27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
ost0 = ost1 = ost2 = ost3 = ost4 = 0
for i in range(len(a)):
    if a[i] % 5 == 0:
        ost0 += 1
    elif a[i] % 5 == 1:
        ost1 += 1
    elif a[i] % 5 == 2:
        ost2 += 1
    elif a[i] % 5 == 3:
        ost3 += 1
    else:
        ost4 += 1

print(ost1*ost4 + ost2 * ost3 + ost0 * (ost0 - 1) //2)
