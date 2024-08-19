def f(n):
    if n < 7:
        return 6
    if n >= 7:
        return n + f(n - 1)

import sys
sys.setrecursionlimit(7777)
print(f(2023)-f(2021))
