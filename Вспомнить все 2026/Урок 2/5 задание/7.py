
def ss(n):
    s = ''
    while n > 0:
         s += str(n % 3)
         n //= 3
    return s[::-1]

for n in range(1, 1000):
    n3 = ss(n)
    if n % 3 == 0:
        n3 += n3[-3:]
    else:
        ost = n % 3
        ost *= 3
        ost3 = ss(ost)
        n3 += ost3

    r = int(n3, 3)
    if r <= 138:
        print(r)