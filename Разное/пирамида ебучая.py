N = int(input('КОЛИЧЕСТВО СТУПЕНЕЙ: '))
b = input('Ваша буква: ')
t = ' '
n = N * 2
c = (n//2) + 1
num = ord(b)
for i in range(1, n+1, 2):
    s = ''
    mid = (i//2)+1
    s += ''.join([chr(num+j) for j in range(mid)])
    # for j in range(mid):
    #     s += chr(num+j)
    c += -1
    r = ''
    if i > 1:
        s += ''.join([chr(num+(i-x)) for x in range(mid+1, i+1)])
        # for x in range(mid+1, i+1):
        #     s += chr(num+(i-x))
    print(c * t + s)