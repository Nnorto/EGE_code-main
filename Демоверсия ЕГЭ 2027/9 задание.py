cnt = 0
f = open('9.txt')
for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    # if len(set(a)) == 5:
    if a[0] < a[1] < a[2] < a[3] < a[4]:
        if 2*(a[0] + a[4]) > a[1] + a[2] + a[3]:
            cnt += 1
print(cnt)

# Ответ: 4874