f = open('Файлы/26_ege22_rezerv.txt')
n = int(f.readline())
a = [int(x) for x in f]
free = n // 5
a.sort()
anwk = sum(a[free + 1:])
anwp = sum(a[:n - free])
print(anwp, anwk)