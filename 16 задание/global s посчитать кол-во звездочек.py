def f(n):
    global k
    k += 1
    if n >= 1:
        k += 1
        f(n - 1)
        f(n - 2)
        k += 1


k = 0
f(35)
print(k)
# answ = 96631265