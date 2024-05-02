a = []
for s in open("17-1.txt"):
    a.append(int(s))

print(a)

b = list(map(int, open("17-1.txt")))

print(*b)

c = [int(s) for s in open("17-1.txt")]

print(c)
