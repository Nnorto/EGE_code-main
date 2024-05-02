s = open('24 файл').readline()
count = 0
max_p = 0
for i in s:
    if i == 'C':
        count += 1
        max_p = max(max_p, count)
    else:
        count = 0
print(max_p)