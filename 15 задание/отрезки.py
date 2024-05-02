"""
Наибольшее -> remove
наименьшее -> add
"""

p = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
a = list(range(40))

for x in range(40):
    if not(((x in a) <= (x in p) ) and ( (x in q) <= (not(x in a)))):
        a.remove(x)

print(a)