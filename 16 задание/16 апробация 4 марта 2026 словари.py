f = {}

for n in range(0, 2025):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n * f[n - 1]

print((f[2024] - 2 * f[2023]) / f[2022])

# 4090506 - ответ