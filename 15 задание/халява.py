"""
(2m + 3n > 40) ∨ ((m < A) ∧ (n ≤ A))

 """

for a in range(1, 500):
    count = 0
    for n in range(0, 999):
        for m in range(0, 999):
            if (2 * m + 3 * n > 40) or ((m < a) and (n <= a)):
                count += 1
            else:
                break
    if count == 998001:
        print(a)

