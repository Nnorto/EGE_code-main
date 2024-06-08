def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * f(n - 1)

import sys
sys.setrecursionlimit(7777)

print((f(2024) - 4 * f(2023)) // f(2022))