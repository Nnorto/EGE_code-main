f = open('26.txt')
n, k = map(int, f.readline().split())
a = []
for s in f:
    nums = s.split()
    if len(nums) == 2:
        a.append([int(nums[0]), 'RED'])
        a.append([int(nums[1]), 'BLUE'])
    else:
        a.append([int(nums[0]), 'RED'])
a.sort(reverse=True)
first_box = a[0]
dlina_first = a[0][0]
color_first = a[0][1]
k_box = 1
for i in range(1, len(a)):
    dlina, color = a[i]
    if dlina_first - dlina >= 3 and color != color_first:
        dlina_first = dlina
        color_first = color
        k_box += 1
        print(dlina_first)
        print(color_first)

print(k_box, dlina_first)




