b = [-42, -10, -8, 2, 16]
c = [-10, -4, 2, 15, 23]
n = b + c
max_s = -1000
a = []
for x in range(len(n)):
    for i in range(len(b)):
        for j in range(len(c)):
            if (n[x] <= b[i]) or c[j]:
                a.append(n[x])
# просто нахожу все числа которые удовлетворяют условию

a = list(set(a))
# из-за вложенности создаются копии элементов
# поэтому оставляю уникальные значения
s = 0
for i in range(len(a)):
    s += a[i]
    max_s = max(max_s, s)
# ну вот и максимальная сумма
print(max_s)