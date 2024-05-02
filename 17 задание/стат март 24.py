f = open('17 файлы/17stat_fev24.txt')
a = [int(x) for x in f]
max8 = max([int(x) for x in a if abs(x) % 1000 == 821])
min8 = min([int(x) for x in a if abs(x) % 1000 == 821])
ss = max8 + min8
res = []
for i in range(len(a) - 3):
    k5 = ((10000 <= a[i] <= 99999) + (10000 <= a[i + 1] <= 99999) + (10000 <= a[i + 2] <= 99999) +
          (10000 <= a[i + 3] <= 99999))
    k3 = (100 <= a[i] <= 999) + (100 <= a[i+1] <= 999) + (100 <= a[i+2] <= 999) + (100 <= a[i+3] <= 999)
    num5 = (a[i] % 5 == 0) + (a[i + 1] % 5 == 0) + (a[i + 2] % 5 == 0) + (a[i + 3] % 5 == 0)
    num7 = (a[i] % 7 == 0) + (a[i + 1] % 7 == 0) + (a[i + 2] % 7 == 0) + (a[i + 3] % 7 == 0)
    if k5 > k3 and num5 == num7:
        s = a[i] + a[i + 1] + a[i + 2] + a[i + 3]
        if s > 2*ss:
            res.append(s)

print(len(res), max(res))

res = []
max8=max([int(x) for x in a if abs(x)%1000==821])
min8=min([int(x) for x in a if abs(x)%1000==821])
for i in range(len(a)-3):
    if (10000<=a[i]<=99999) + (10000<=a[i+1]<=99999) + (10000<=a[i+2]<=99999) + (10000<=a[i+3]<=99999) > (100<=a[i]<=999) + (100<=a[i+1]<=999) + (100<=a[i+2]<=999) + (100<=a[i+3]<=999):
        if (a[i]%5==0) + (a[i+1]%5==0) + (a[i+2]%5==0) + (a[i+3]%5==0) == (a[i]%7==0) + (a[i+1]%7==0) + (a[i+2]%7==0) + (a[i+3]%7==0):
            if (a[i]+a[i+1]+a[i+2]+a[i+3])>(min8+max8)*2:
                res.append(a[i]+a[i+1]+a[i+2]+a[i+3])
print(len(res), max(res))

max8 = max([int(x) for x in a if abs(x) % 1000 == 821])
min8 = min([int(x) for x in a if abs(x) % 1000 == 821])
ss = max8 + min8
res = []
for i in range(len(a) - 3):
    k5 = ((10000 <= a[i] <= 99999) + (10000 <= a[i + 1] <= 99999) + (10000 <= a[i + 2] <= 99999) +
          (10000 <= a[i + 3] <= 99999))
    k3 = (100 <= a[i] <= 999) + (100 <= a[i + 1] <= 999) + (100 <= a[i + 2] <= 999) + (100 <= a[i + 3] <= 999)
    p5 = (a[i] % 5 == 0) + (a[i+1] % 5 == 0) + (a[i+2] % 5 == 0) + (a[i+3] % 5 == 0)
    p7 = (a[i] % 7 == 0) + (a[i+1] % 7 == 0) + (a[i+2] % 7 == 0) + (a[i+3] % 7 == 0)

    if p5 == p7 and k5 > k3:
        s = a[i] + a[i + 1] + a[i + 2] + a[i + 3]
        if s > ss * 2:
            res.append(s)

print(len(res), max(res))


