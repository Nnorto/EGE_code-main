# пришел
ch1 = int(input())
m1 = int(input())
s1 = int(input())
# ушел
ch2 = int(input())
m2 = int(input())
s2 = int(input())

time1 = ch1 * 3600 + m1 * 60 + s1
time2 = ch2 * 3600 + m2 * 60 + s2
time = time2 - time1
print(time, "сек")
ch3 = time // 3600
m3 = (time - 3600 * ch3) //60
s3 = time - (3600 * ch3) - (60 * m3)
print( ch3, "часы", m3,"мин ", s3, "сек")