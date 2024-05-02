a = [int(s) for s in open("17 файлы/17-1.txt")]
count = 0
max_sum = -131212311231231312

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[j] % 3 == 0 or a[i ] % 3 == 0:
            count += 1
            max_sum = max(max_sum, a[i] + a[j])

print(count, max_sum)