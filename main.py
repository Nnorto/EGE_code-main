n = int(input())
a = 1
b = 0
step = 1
res = 0
while step < n:
    res = a + b
    b = a
    a = res
    step += 1
print(res)
