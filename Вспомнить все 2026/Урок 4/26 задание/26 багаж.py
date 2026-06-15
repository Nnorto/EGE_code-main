f = open('26 багаж.txt')
cnt_box = int(f.readline())
cnt_passaj = int(f.readline())
cnt = 0
id_box = 0
passaj = []
box = [0]*cnt_box
for s in f:
    time_start, time_end = [int(x) for x in s.split()]
    passaj.append([time_start, time_end])
passaj.sort()
for star, finish in passaj:
    for i in range(len(box)):
        if star > box[i]:
            box[i] = finish
            cnt += 1
            id_box = i + 1
            break

print(cnt, id_box)