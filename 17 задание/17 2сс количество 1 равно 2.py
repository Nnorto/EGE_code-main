a = list(map(int, open("17statokt23.txt")))
count = 0
max_sum = -1
for i in range(len(a) - 2):
    if bin(a[i]).count("1") == 2 and bin(a[i]).count("1") == 2 and bin(a[i]).count("1") == 2:
        count += 1
        max_sum = max(max_sum, (a[i] + a[i + 1] + a[i + 2]))

print(count, max_sum)