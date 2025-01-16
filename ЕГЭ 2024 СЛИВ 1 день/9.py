f = open('9-4.txt')
count = 0
for s in f:
    a = [int(el) for el in s.split()]
    a.sort()
    if a[0] < a[1] < a[2] < a[3]:
        if a[3] < a[0] + a[1] + a[2]:
            count += 1
print(count)
