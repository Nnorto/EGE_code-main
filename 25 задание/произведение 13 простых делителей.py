def dell(n):
    d = []
    for i in range(2, int(n**0.5) +1):
       while n % i == 0:
            d.append(i)
            n //= i
    if  n > 1:
        d.append(n)
    if len(d) == 13 and '1' in str(sum(d)):
        return d
    return 0

p = 0

for n in range(987_654_320, 1, -1):
    d = dell(n)
    if d:
        print(n, max(d))
        p += 1
        if p == 5:
            break
