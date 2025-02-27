import sys
def f(n):
    if n < 5:
        return n
    return 2 * n * f(n - 4)
sys.setrecursionlimit(100000)
print((f(13766) - 9 * f(13762)) / f(13758))