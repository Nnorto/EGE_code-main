def f(n):
    global s
    s += n + 1
    if n > 1:
        s +=  2* n
        f(n - 1)
        f(n - 3)

for n in range(1, 10**10):
    s = 0
    f(n)
    if s > 10**6:
        print(n, s)
        break

