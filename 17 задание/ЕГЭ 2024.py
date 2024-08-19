a = [int(s) for s in open("ЕГЭ 2024 СЛИВ 1 день/2024_Файлы/17 реальное.txt")]
count = 0
max_sum = -131212311231231312
minel = min(a)

for i in range(len(a) - 1):
    if a[i] % 18 + a[i + 1] % 18 == minel:
        count += 1
        max_sum = max(max_sum, a[i] + a[i + 1])
print(count, max_sum)