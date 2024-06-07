f=open("26h.txt")
n,rad,mes=map(int,f.readline().split())
mest=[[0 for i in range(rad+1)]for j in range(mes+1)]

for s in f:
    q,z=map(int,s.split())
    mest[z][q]=1
mest.sort()
for i in range(1,mes + 1):
    print(*mest[i])

maxk=-1
res=0
for i in range(1,mes + 1):
    k0=0
    for j in range(1,rad + 1):
        if mest[i][j]==0:
            k0+=1
            if k0>maxk:
                maxk=k0
                res=j
            elif k0==maxk:
                res=min(res,j)
        else:
            if k0 > 0:
                break
            k0=0
print(res,maxk-1)