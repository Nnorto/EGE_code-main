from functools import *
import sys

@lru_cache(None)
def g(h):
    a, b = h  # 0, 10 or 1, 10
    m = []
    if a > 1:
        m.append((a // 2 + a % 2, b))
    if b > 1:
        m.append((a, b // 2 + b % 2))
    if a > 3:
        m.append((a - 2, b))
    if b > 3:
        m.append((a, b - 2))
    if a + b <= 40:
        return 'w'
    if any(g(x) == 'w' for x in m):
        return 'p1'
    if all(g(x) == 'p1' for x in m):
        return 'v1'
    if any(g(x) == 'v1' for x in m):
        return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m):
        return 'v2'

p1, v1, p2, v2 = [], [], [], []
for s in range(20, 100+1):
    h = 20, s
    if g(h) == 'p1':
        p1.append(s)
    if g(h) == 'v1':
        v1.append(s)
    if g(h) == 'p2':
        p2.append(s)
    if g(h) == 'v2':
        v2.append(s)

print('p1', p1)
print('v1', v1)
print('p2', p2)
print('v2', v2)