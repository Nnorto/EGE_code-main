f = open("C:/Users/lucky/PycharmProjects/EGE_code-main/27 задание/27 файлы/27_B_1_day.txt")

k = int(f.readline())
N = f.readline()
a = list(map(int,f))

min1s = min2s = min3s = 10**10
for i in range(2 * k, len(a)):
    min1s = min(min1s, a[i - 2 * k])
    min2s = min(min2s, a[i - k] + min1s)
    min3s = min(min3s, a[i] + min2s)

print(min3s)