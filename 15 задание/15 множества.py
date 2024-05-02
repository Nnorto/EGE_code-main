B=[-42,-10,-8,2,16]
C=[-10,-4,2,15,23]
A=[x for x in range(1000)]
Aa=[]
for x in range(1000):
    if ((x in A)<=(x in B)) or (x in C):
            Aa.append(A[x])
print(sum(Aa))