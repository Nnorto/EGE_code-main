a = list(map(int, open('17 (1).txt')))
min_3 = [x for x in a if 99 < x < 1000]
min_3.sort()
# минимального трёхзначного элемента последовательности
n = min_3[1]
count = 0
max_sum = -1
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) < n * n:
        count += 1
        max_sum = max(max_sum, a[i] + a[i + 1])

print(count, max_sum)