from functools import *
@lru_cache(None)
def f(n):
    if n < 10:
        return 3
    return (n + 4) * f(n - 5)

for i in range(10, 257777):
    f(i)

print((f(257487)// 683 + 67 * f(257477)) // f(257472))

# или

f = {}
for n in range(1, 257777):
    if n < 10:
        f[n] = 3
    else:
        f[n] = (n + 4) * f[n - 5]
print((f[257487]// 683 + 67 * f[257477]) // f[257472])