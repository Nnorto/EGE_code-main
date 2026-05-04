f = {}
for n in range(1, 5000):
    if n < 10:
        f[n] = n - 1
    if n >= 10 and n % 2 == 0:
        f[n] = 3 * n - 1 + f[n - 3]
    if n >= 10 and n % 2 != 0:
        f[n] = 5*n + 2 + f[n - 4]
print(f[4445] - f[4444])