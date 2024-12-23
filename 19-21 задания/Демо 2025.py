from functools import lru_cache
@lru_cache(None)
def g(h):
    m = [h//3, h - 5, h - 2] # все возможные ходы
    if h <= 19: return 'win'
    if any(g(x) == 'win' for x in m): return 'p1'
    if all(g(x) == 'p1' for x in m):  return 'v1' #мина
    if any(g(x) == 'v1' for x in m): return 'p2'
    if all(g(x) == 'p1' or g(x) == 'p2' for x in m): return 'v1orv2'


v1, p2, v12 = [], [], []
for s in range(20, 100 + 1):
    if g(s) == 'v1':
        v1.append(s)
    if g(s) == 'p2':
        p2.append(s)
    if g(s) == 'v1orv2':
        v12.append(s)
print(f'19 задание: {v1[0]}')
print(f'20 задание: {p2[0]}, {p2[1]}')
print(f'21 задание: {v12[0]}')

# 19 задание: 60
# 20 задание: 62, 63
# 21 задание: 64