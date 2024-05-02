f = open('17 файлы/17stat_fev24.txt')
a = [int(x) for x in f]
min3 = max([int(x) for x in a if abs(x) % 1000 == 832])

res = []
for i in range(len(a)-2):
    if 1<=(1000<=a[i]<=9999) + (1000<=a[i+1]<=9999) + (1000<=a[i+2]<=9999)<=2:
        num5 = (a[i]%5==0) + (a[i+1]%5==0) + (a[i+2]%5==0)
        num3 = (a[i]%3==0) + (a[i+1]%3==0) + (a[i+2]%3==0)
        if num5 > num3:
            if (a[i]+a[i+1]+a[i+2])>min3:
                res.append(a[i]+a[i+1]+a[i+2])

print(len(res), max(res))
