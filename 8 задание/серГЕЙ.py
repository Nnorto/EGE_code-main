import itertools

s = "СЕРГЕЙ"

count = set()

for x in itertools.product(s, repeat=5):
    a = ''.join(x)
    if (a.count("Й") <= 1) and (a[0] != "Й") and (a[4] != "Й") and ("ЙЕ" not in a) and ("ЕЙ" not in a):
        count.add(a)

print(len(count))
