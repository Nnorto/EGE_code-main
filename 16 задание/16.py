f = {}
g = {}
for n in range(22600, -10, -1):
    if n >= 22560:
        g[n] = n // 23 + 33
    if n < 22560:
        g[n] = g[n + 11] - 4

for n in range(1, 600):
    if n >= 21:
        f[n] = f[n - 8] + 1095
    if n < 21:
        f[n] = 10 * (g[n - 7] - 36)

print(f[548])
