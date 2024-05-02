import sys
def f(n):
    if n > 10000:
        return 42
    if n <= 10000 and n % 2 == 0:
        return 2 * n + f(n + 3) + f(n + 4) + f(n + 6)
    else:
        return -1*(n + f(n + 1) + f(n + 3))

sys.setrecursionlimit(10001)

print(f(9996) - f(9994))
