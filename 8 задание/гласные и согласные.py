import itertools


def f(a):
    gl = ["А", "Е"]
    sogl = ["Т", "С"]
    for i in range(len(a) - 1):
        if (a[i] in sogl and a[i + 1] in sogl) or (a[i] in gl and a[i + 1] in gl):
            return True



s = "АТТЕСТАТ"

res = set()


for x in itertools.permutations(s):
    a = ''.join(x)
    if f(a):
        res.add(a)

print(len(res))
