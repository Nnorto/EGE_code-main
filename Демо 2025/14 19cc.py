alf19 = '0123456789ABCDEFGHI'
for x in alf19:
    t1 = int(f'98897{x}21', 19)
    t2 = int(f'2{x}923', 19)
    s = t1 + t2
    if s % 18 == 0:
        print(x, s // 18)
# F 469034148 - ответ

for x in range(19):
    t1 = int('98897021', 19) + x * 19**2
    t2 = int('20923', 19) + x * 19**3
    s = t1 + t2
    if s % 18 == 0:
        print(x, s // 18)

# 15 469034148 - ответ