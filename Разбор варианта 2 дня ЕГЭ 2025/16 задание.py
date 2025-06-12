f = {}
g = {}

for n in range(1, 52000):
    if n <= 7:
        f[n] = n
    if n > 7:
        f[n] = g[n - 3] * 3
    if n <= 7:
        g[n] = n
    if n > 7:
        g[n] = g[n - 1] + 4

print(f[43000])