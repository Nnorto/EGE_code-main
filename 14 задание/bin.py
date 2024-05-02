print(bin(8**1023+2**1024-3)[2:].count('1'))

n1 =8**1023+2**1024-3
k = 0
while n1 > 0:
    if n1 % 2 == 1:
        k += 1
    n1 //= 2

print(k)

n1 = 4**2014+2**2015-9
s = ''
while n1 > 0:
    s = str(n1 % 2) + s
    n1 //= 2
print(s.count('0'))