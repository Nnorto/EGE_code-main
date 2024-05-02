# № 1 решение в лоб
print('1) ' + '='*10)

for a in range(1, 500):
    kx = 0
    for x in range(1, 500):
        if (x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0)):
            kx += 1
    if kx == (500 - 1):
        print(a)



# № 2 через флажки
print(end='\n\n')
print('2) ' + '='*10)

for a in range(1, 500):
    flag = True
    for x in range(1, 500):
        if ((x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0))) == 0:
            flag = False
    if flag:
        print(a)



# № 3 через for -> else
print(end='\n\n')
print('3) ' + '='*10)

for a in range(1, 500):
    for x in range(1, 500):
        if ((x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0))) == 0:
            break
    else:
        print(a)

# № 4 через all (имба, решает намного быстрее)
print(end='\n\n')
print('4) ' + '=' * 10)

for a in range(1, 500):
    if all((x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0)) for x in range(1, 500)):
       print(a)


