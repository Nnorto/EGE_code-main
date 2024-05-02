f = open('27 файлы/27-B.txt')
n = int(f.readline())
k = 4
a = [int(x) for x in f]
res = k29 = k1 = 0
ki29 = vse29 = ki1 = 0

for i in range(k):
    if a[i] % 29 == 0:
        vse29 += ki29 + ki1
        ki29 += 1
    else:
        vse29 += ki29
        ki1 += 1

for i in range(k, len(a)):
    if a[i - k] % 29 == 0:
        k29 += 1
    else:
        k1 += 1

    if a[i] % 29 == 0:
        res += k29 + k1
        vse29 += ki29 + ki1
        ki29 += 1

    else:
        res += k29
        vse29 += ki29
        ki1 += 1

print(vse29 - res)
print(ki29 * (ki29 - 1) // 2 + ki29 * ki1 - res)

# vse29 - res победа изи 2б
#A 143
#B 291675


