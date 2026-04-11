f = {}
for n in range(257500):
    if n < 10:
        f[n] = 3
    if n >= 10:
        f[n] = (n + 4) * f[n - 5]
print((f[257487] // 683 + 67 * f[257477]) // f[257472])

# #24994270044009

from functools import *

@lru_cache(None)
def f(n):
    if n < 10:
        return 3
    return (n + 4) * f(n - 5)

for i in range(257500): f(i)

print((f(257487) // 683 + 67 * f(257477)) // f(257472))


