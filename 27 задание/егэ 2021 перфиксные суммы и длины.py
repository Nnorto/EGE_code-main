f = open('27 файлы/27-B1.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = 100
si = 0
mins, minlen = 10**20, 10**20
prefs = [0]*k
preflen = [0]*k

for i in range(len(a)):
    si += a[i]
    leni = i + 1  # текущая длина
    if si % 100 == 0 and si < mins:
        mins = si
        minlen = leni
    maybe_sum = si - prefs[si % k]  # возможная сумма которая кратна 100
    maybe_len = leni - preflen[si % k]  # возможная длина такой суммы
    if (maybe_sum < mins) or (maybe_sum == mins and maybe_len < minlen):
        mins = maybe_sum
        minlen = maybe_len
    prefs[si % k] = si
    preflen[si % k] = leni

print(mins, minlen)