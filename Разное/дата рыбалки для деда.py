d = int(input())
m = int(input())
g = int(input())

if d == 1 and m == 12:
    print('31.12.', g - 1, sep='')
elif d == 1 and m == 3:
    print(f'28.{m - 1}.{g} ')
elif d == 1 and (m == 1 or m == 5 or m == 7
                 or m == 8 or m == 10
                 or m == 12):
    print(f'30.{m - 1}.{g}')
elif d == 1 and (m == 2 or m == 4 or
                 m == 6 or m == 9 or m == 11):
    print(f'31.{m - 1}.{g}')
else:
    print(f'{d - 1}.{m}.{g}')


