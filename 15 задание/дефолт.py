"""
(2x + 3y > 40) ∨ ((x < A) ∧ (y ≤ A))
"""


for a in range(1, 500):
    count = 0
    for x in range(0, 999):
        for y in range(0, 999):
            if (2 * x + 3 * y > 40) or ((x < a) and (y <= a)):
                count += 1
            else:
                break
    if count >= 998001:
        print(a)
