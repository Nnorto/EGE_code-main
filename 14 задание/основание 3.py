n1 = 9 ** 14 + 3 ** 18 - 9 ** 5 - 81
k = 0
while n1 > 0:
    if n1 % 3 == 2:
        k += 1
    n1 //= 3

print(k)

n1 = 9 ** 14 + 3 ** 18 - 9 ** 5 - 81
s = ''
while n1 > 0:
    s = str(n1 % 3) + s
    n1 //= 3
print(s.count('2'))