f = open('27 файлы/27_B.txt')
n = int(f.readline())
a = [int(x) for x in f]
k26 = k13 = k2 = k1 = res = 0
vse = 0
for i in a:
    vse += k26 + k13 + k2 + k1
    if i % 26 == 0:
        res += k26 + k13 + k2 + k1
        k26 += 1
    elif i % 13 == 0:
        res += k26 + k2
        k13 += 1
    elif i % 2 == 0:
        res += k26 + k13
        k2 += 1
    else:
        res += k26
        k1 += 1

print(vse - res)


