import shutil


def s3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    s = s[::-1]
    return s

a = []
for n in range(1, 12312):
    n3 = s3(n)
    summ_1 = n3.count('1') + n3.count('2')*2
    summ_2 = sum([int(x) for x in n3])
    if summ_2 % 2 == 0:
        n3 = '1' + n3 + '2'
    else:
        n3 = '2' + n3 + '0'

    r = int(n3, 3)
    if r > 100:
        a.append(r)

print(min(a))