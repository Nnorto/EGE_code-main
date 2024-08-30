mr = -1000000
for n in range(1, 12 + 1):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = '10' + n2
    else:
        n2 = '1' + n2 + '01'
    r = int(n2, 2)
    mr = max(mr, r)

print(mr)