f = open('2024_Файлы/27_B_2024.txt')
n = int(f.readline())
m1 = m2 = m3 = -10**100
a = [int(x) for x in f]
for i in range(n - 2):
    m1 = max(m1, a[i - 2])
    m2 = max(m2, m1 - 2 * a[i - 1])
    m3 = max(m3, m2 + a[i])
print(m3)