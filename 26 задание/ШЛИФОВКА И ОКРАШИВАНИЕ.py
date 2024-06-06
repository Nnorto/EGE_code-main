f = open('Файлы/26-129.txt')
n = int(f.readline())
a = []
for s in f:
    ns = s.split()
    a.append([int(ns[0]), int(ns[1])])
det = []
n = 0
for i in range(len(a)):
    x = a[i][0]
    y = a[i][1]
    if x < y:
        det.append([x, "ш", i])
    else:
        det.append([y, "о", i])


det.sort()
lenta, s = [], 0
last = res1 = 0
for i in range(len(det)):
    lenta.append(det[i][2])
    if det[i][1] == "ш":
        s += 1
    last = det[i][1]
    res1 = det[i][2] + 1

if last == "ш":
    print(res1, s - 1)
else:
    print(res1, s)

# OR

f = open('Файлы/26-129.txt')
num=int(f.readline())
l=[]
conv=[-1]*num
n=0
for s in f:
    n+=1
    a,b=map(int,s.split())
    if a<b:
        l.append([a,"S",n])
    else:
        l.append([b,"O",n])
l.sort()
count=0
last=0
for i in range(n):
    if l[i][1]=="S":
        for j in range(num):
            if conv[j]==-1:
                conv[j]=l[i][0]
                last=l[i][2]
                count+=1
                break
    if l[i][1]=="O":
        for j in range(num-1,-1,-1):
            if conv[j]==-1:
                conv[j]=l[i][0]
                last=l[i][2]
                break
print(count-1,last)