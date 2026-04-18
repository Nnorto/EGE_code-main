f = {}
g = {}

for n in range(250_000, -10, -1):
    if n >= 248045:
        g[n] = n / 20 + 28
    if n < 248045:
        g[n] = g[n + 9] - 4

for n in range(1, 680):
    if n >= 19:
        f[n] = f[n - 4] + 3580
    if n < 19:
        f[n] = 6 * (g[n - 7] - 36)

print(f[673])

# 47 - ответ