from functools import lru_cache
@lru_cache(1000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * f(n - 1)

for i in range(1, 10999): f(i)
print((f(10938) // 2 - f(10937)) // f(10936))