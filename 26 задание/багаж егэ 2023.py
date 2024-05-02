f = open("Файлы/26_ege23_dosrok.txt")
k = int(f.readline())
n = int(f.readline())
count = 0
last = 0
pip = []
box = [-1]*k
for i in range(n):
    x, y = map(int, f.readline().split())
    pip.append([x, y])
pip.sort()

for i in range(len(pip)):
    start = pip[i][0]
    fin = pip[i][1]
    for box_index in range(len(box)):
        if start > box[box_index]:
            box[box_index] = fin
            count += 1
            last = box_index + 1
            break

print(count, last)