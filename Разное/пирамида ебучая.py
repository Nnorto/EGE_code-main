b = input()
t = ' '
c = 7
num = ord(b)
for i in range(1, 10+1, 2):
    s = ''
    mid = (i//2)+1
    for j in range(mid):
        s += chr(num+j)
    c += -1
    r = ''
    if i > 1:
        for x in range(mid+1, i+1):
            s += chr(num+(i-x))
    print(c * t + s)