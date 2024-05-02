f=open("27 файлы/27_A_1_day.txt")
k=int(f.readline())
N=f.readline()
a=list(map(int,f))
minc=10**10
for i in range(len(a)):
    for j in range(i+k,len(a)):
        for q in range(j+k,len(a)):
            minc=min(minc,a[i]+a[j]+a[q])
print(minc)

f = open("27 файлы/27_B_1_day.txt")

k = int(f.readline())
N = f.readline()
a = list(map(int,f))

min1s = min2s = min3s = 10**10
for i in range(2 * k, len(a)):
    min1s = min(min1s, a[i - 2 * k])
    min2s = min(min2s, a[i - k] + min1s)
    min3s = min(min3s, a[i] + min2s)

print(min3s)

