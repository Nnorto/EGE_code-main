def f(num, sist):
    res = ""
    while num > 0:
        res = str(num % sist) + res
        num //= sist
    return res


s = 0
summa = 0
for n in range(1, 95):
    n3 = f(n,3)
    n5 = f(n,5)
    if n3[-2:] == '21' and n5[0] == '3':
        summa += n
print(summa)
