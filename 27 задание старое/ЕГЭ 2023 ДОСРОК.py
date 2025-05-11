f=open("27пример")
N = int(f.readline())
k = int(f.readline())
a=list(map(int,f))
maxc=0
for i in range(len(a)):
    for j in range(i+k,len(a)):
        maxc=max(maxc,a[i]+a[j])
print(maxc)