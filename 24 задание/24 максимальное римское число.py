f_rim = open('24 все коректные римские числа')
rim_num = []
for s in f_rim:
    a, b = [x for x in s.split()]
    a = int(a)
    rim_num.append([a, b])
rim_num.sort(reverse=True)
print(rim_num[:3])

s = open('Файлы/24_31160.txt').readline()
md = 0
for a, b in rim_num:
    if b in s and len(b) >= md:
        md = len(b)
        print(a, b)