f=[0]*2026
f[1] = 2
for n in range(2, 2026):
    f[n] += f[n-1] + n+2
g = [0]*2026
for n in range(2, 2026):
    g[n] = g[n-1] + f[n]*20


print(f[2025]*200-g[2025])