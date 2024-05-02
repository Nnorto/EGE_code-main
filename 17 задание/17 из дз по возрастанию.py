a = []
with open('17-1.txt') as f:
    for n in f:
        n = int(n)
        a.append(n)
# забыл рассказать о таком способе чтения, так тоже можно, но сложнее

k = 0
minim =20001
for i in range(len(a) -2):
    if a[i] < a[i + 1] < a[i + 2]:
        k += 1
    minim = min(minim, a[i+2] - a[i])
print(k, minim)