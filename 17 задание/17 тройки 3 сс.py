a = [int(s) for s in open("17 файлы/17-1.txt")]
count = 0
min_sum = 131212311231231312

for i in range(len(a) - 2):
    for j in range(i + 1, len(a) - 1):
        for z in range(j + 1, len(a)):
            if a[i] % 3 == 2 or a[j] % 3 == 2 or a[z] % 3 == 2:
                count += 1
                min_sum = min(min_sum, a[i] + a[j] + a[z])

print(count, min_sum)
