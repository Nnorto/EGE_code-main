'''
ДЕЛ(120, A) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 18) → ¬ДЕЛ(x, 24)))

Раскладываем на простейшие булевы операции, тк в python 0 != False и 1 != True
'''


def dell(x, a):
    return x % a == 0


for a in range(1, 101):
    count = 0
    for x in range(1, 10000):
        if dell(120, a) and (dell(x, a) or (not dell(x, 18)) or (not dell(x, 24))):
            count += 1
        if count >= 9999:
            print(a)
