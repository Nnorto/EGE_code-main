f = {}

for n in range(1, 7000):
    if n < 10:
        f[n] = n
    if n >= 10:
        f[n] = 3*n + f[n - 3]

print((f[6250] + 2 * f[6244]) // f[6238])