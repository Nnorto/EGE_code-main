

"¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 9))"
def dell(x, a):
    return x % a == 0

for a in range(1, 500):
    count = 0
    for x in range(0, 999):
        if (not(not dell(x, a))) or (not(dell(x, 6))) or (not(dell(x, 9))):
            count += 1
        else:
            break
    if count == 999:
        print(a)
