n = int(input())
a = 1
fn = 0 + 1
for x in range(n-2):
    b = fn
    fn = a + fn
    a = b
print(fn)

