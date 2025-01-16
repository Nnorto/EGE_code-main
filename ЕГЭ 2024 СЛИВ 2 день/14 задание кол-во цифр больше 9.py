def ss(n, k):
    count = 0
    while n > 0:
        if n % k > 9:
            count += 1
        n //= k
    return count

n = 2*729**2014 + 2*243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2*9**2022 - 2024
print(ss(n, 27))

# или
def ss(n, k):
    s = []
    while n > 0:
        s = [str(n % k)] + s
        n //= k
    return s

n = 2*729**2014 + 2*243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2*9**2022 - 2024
res = ss(n, 27)
count = 0
for i in range(len(res)):
    if int(res[i]) > 9:
        count += 1
print(count)
