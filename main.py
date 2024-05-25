import sys

def f(n):
    if n < 2:
        return 2
    if n > 12 and n % 2 != 0:
        return n + f(n - 1)
    else:
        s = 0
        for i in range(1, n):
            s += f(i)
        return s

print(f(15))