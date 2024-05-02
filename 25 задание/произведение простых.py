def prime(n):
    vd=[]
    for d in range(2,int(n**0.5)+1):
        if n%d==0 and d*d!=n:
            if prost(n/d) and prost(d):
                vd.append(d)
                vd.append(n//d)
    return vd
def prost(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n%d==0:
            return False
    return True
minch=10**10
k=0

for n in range(268312,336493):
    if len(prime(n))>1:
        k+=1
        minch=min(minch,n)

print(minch,k, )