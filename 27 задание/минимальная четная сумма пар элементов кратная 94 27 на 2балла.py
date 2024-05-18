f = open('27 задание/27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 94
minch = [10**10]*k
mins = 10*10
for i in range(len(a)):
    ost = a[i] % k
    ostnap = (k - ost) % k
    mins = min(mins, a[i] + minch[ostnap])
    minch[ost] = min(minch[ost], a[i])

print(mins)

f = open('27 задание/27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 94
minch = [10**10]*k
mins = 10*10
for i in range(len(a)):
    ost = a[i] % k
    ostnap = (k - ost) % k
    if a[i] + minch[ostnap] % 2 == 0:
        mins = min(mins, a[i] + minch[ostnap])
        minch[ost] = min(minch[ost], a[i])

print(mins)


f = open('27 задание/27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 94
minch = [10**10]*k
minnch = [10**10]*k
mins = 10*10
for i in range(len(a)):
    ost = a[i] % k
    ostnap = (k - ost) % k
    if a[i] % 2 == 0:
        mins = min(mins, a[i] + minch[ostnap])
        minch[ost] = min(minch[ost], a[i])
    else:
        mins = min(mins, a[i] + minnch[ostnap])
        minnch[ost] = min(minnch[ost], a[i])

print(mins)

